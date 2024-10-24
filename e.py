import os, string

list = str(input().split())
with open(r"/Users/askarovva/Desktop/lab6.2/example.txt",'w') as here:
    here.write(list)