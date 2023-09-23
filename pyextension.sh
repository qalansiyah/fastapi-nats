#!/bin/sh
gcc -shared -o count_and_avg.so -fPIC count_avg.c  -I/usr/include/python3.11 -I/usr/include

