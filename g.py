with open(r"/Users/askarovva/Desktop/lab6.2/example.txt",'r') as first:
    with open(r"/Users/askarovva/Desktop/lab6.2/example2.txt",'w') as here:
        for line in first:
            here.write(line)