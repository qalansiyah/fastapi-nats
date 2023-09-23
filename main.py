import asyncio
import datetime
import uvicorn
from fastapi import FastAPI 
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from nats.aio.client import Client
import sqlite3
import json
#Import a library written in C for counting occurrences and computing averages
import count_and_avg

letter = 'X' #Setting the value of the variable 'letter

nc = Client() #Creating a NATS client instance

class Book(BaseModel):  #Defining a data model 
    datetime: str
    title: str
    text: str
book = Book(datetime="datetime", title="title", text="text")
json_data = jsonable_encoder(book) #Encoding the book object to JSON format
json_data["datetime"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")

#Defining a function to count occurrences of a letter in a given text 
def count_in_line(text : str, letter : str) -> int:
    return count_and_avg.count_in_line(text, letter)

#Defining a function to compute the average number of occurrences of a letter in a given text
def avg_in_line(text : str, letter : str) -> float:
    return count_and_avg.avg_in_line(text, letter)

async def connect_nats() -> None:  #Connect to NATS server
    await nc.connect(servers=["nats://nats:4222"])

async def publish_data(nc, json_data) -> None: #Publish data to NATS server
    with open("data.json") as file:
        json_load = json.load(file)
        while True:
            for data in json_load:
                json_data["title"] = data['title']
                json_data["text"] = data['text']
                await nc.publish("data_topic", json.dumps(json_data).encode("utf-8"))
                await asyncio.sleep(3) #Waiting for next post

async def process_data(msg) -> int:#Function to process incoming data from NATS server
    data_dict = json.loads(msg.data.decode("utf-8")) #Decoding data from a message in JSON format
    data_list = data_dict if isinstance(data_dict, list) else [data_dict]
    
    for data in data_list:
        count = count_in_line(data["text"], letter) #Counting the number of characters
        conn = sqlite3.connect('count.db')
        cursor = conn.cursor()
        #SQL query to insert data into a database
        cursor.execute("INSERT INTO books (datetime, title, text,  x_count_in_line) VALUES (?, ?, ?, ?)", (datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f"), data["title"], data["text"], count))
        conn.commit()
        cursor.close()
        conn.close()
    return count

async def subscribe_data(nc) -> None: #Subscribe to the 'data_topic' subject
    await nc.subscribe("data_topic", cb=process_data) 

def create_app():  #Creating a FastAPI application
    app = FastAPI(docs_url='/') #Creating a NATS client instance
    @app.on_event("startup") #Application startup
    async def startup_event() -> None:
        await connect_nats()
        asyncio.create_task(publish_data(nc, json_data)) #Create a task to publish data
        await subscribe_data(nc)

    @app.post("/upload")
    async def upload() -> dict: #Endpoint to handle file uploads
        return {"datetime": json_data["datetime"], "title": json_data["title"], "text": json_data["text"]}

    @app.get("/result")
    async def get_result() -> list:  #Endpoint to get processing results
        #Establishing a connection to the SQLite database 
        conn = sqlite3.connect('count.db')
        cursor = conn.cursor()
        #SQL query to select all rows from 'text' column
        cursor.execute('SELECT text FROM books')
        lines = cursor.fetchall()
        for line in lines:
            avg = avg_in_line(str(line[0]), letter)#Calculating the average
            cursor.execute("UPDATE books SET x_avg_count_in_line = ? WHERE text = ?", (avg, line[0]))
            conn.commit()
        cursor.execute("SELECT datetime, title , x_avg_count_in_line FROM books ")
        result = cursor.fetchall()
        cursor.close()
        #Closing a database connection
        conn.close()

        return [
            {"datetime": row[0], "title": row[1], "x_avg_count_in_line": row[2] }
            for row in result
            ]

    return app
webapp = create_app()

def main():
    uvicorn.run(webapp, host="0.0.0.0", port=8888)
if __name__ == "__main__":
    main()
