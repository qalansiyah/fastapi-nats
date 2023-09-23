#include <Python.h>
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

//Function to count the number of letter characters in the string text
static int counter_in_line(const char* text, const char* letter) {
    int length = strlen(text);
    int total_count = 0;
    
    if (length == 0) {
        printf("Error: String is empty\n");
        return -1;
        }
    
    else{
    
    for (int i = 0; i < length; i++) {
         if (text[i] == *letter) {
              total_count++;
            }
        }
       }             
    
    return total_count;
}

//Function to calculate the average of the letter characters in the string text
static float average_in_line(const char* text, const char* letter) {
    int length = strlen(text);
    int non_space_length = 0;
    
    if (length == 0) {
        printf("Error: String is empty\n");
        return -1;
    }
    
    else{
   
    for (int i = 0; i < length; i++) {
        char ch = text[i];
        if (!isspace(ch) && !ispunct(ch)) {
            non_space_length++;
        }
    }
 }
    if (non_space_length == 0) {
        printf("Error: The string doesn't contain any letter or number\n");
        return -1;
    }
    int count = counter_in_line(text, letter);
    float average_count = (float)count / non_space_length;
    return average_count;
    }
    
//Python wrapper function to call the counter_in_line function
static PyObject* count_in_line(PyObject* self, PyObject* args) {
    const char* text;
    const char* letter;

    //Getting arguments from Python
    if (!PyArg_ParseTuple(args, "ss", &text, &letter)) {
        return NULL;
    }

    int total_count = counter_in_line(text, letter);
    return Py_BuildValue("i", total_count);
}

//Python wrapper function to call average_in_line function
static PyObject* avg_in_line(PyObject* self, PyObject* args) {
    const char* text;
    const char* letter;

    if (!PyArg_ParseTuple(args, "ss", &text, &letter)) {
        return NULL;
    }

    float average_count = average_in_line(text, letter);
    return Py_BuildValue("f", average_count);
}
//Available Extension Methods
static PyMethodDef methods[] = {
    {"count_in_line", count_in_line, METH_VARARGS, "Count the number of char in the text"},
    {"avg_in_line", avg_in_line, METH_VARARGS, "Calculate average value of char in text"},
    {NULL, NULL, 0, NULL},
};

//Definition of expansion module
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "count_and_avg",
    "Extension module",
    -1,
    methods
};

//Initializing the extension module
PyMODINIT_FUNC PyInit_count_and_avg(void) {
    return PyModule_Create(&module);
}

