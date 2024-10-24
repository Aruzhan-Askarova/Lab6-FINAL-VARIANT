import os

here = r"/Users/askarovva/Desktop/lab6.2/example.txt"
if os.path.exists(here):
    print(os.path.basename(here))
    print(os.path.dirname(here))