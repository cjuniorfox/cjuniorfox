#!/usr/bin/python
from datetime import datetime
import os.path

intfile = 0
i=0
while i < 10000 :
    while os.path.exists(str(intfile)+'.txt'):
        intfile +=1
    with open(str(intfile)+'.txt', 'w') as f:
        f.write(str(datetime.now()))
    i += 1
