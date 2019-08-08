import os
import time
from datetime import datetime, timezone

def main():
    i = 0 #comment out this feature when not used in testing

    userdir = input("What subfolder are your files in?")
    tiertag = input("What tier tag would you like to add? (Specific to Dev's needs)")

    for filename in os.listdir(userdir): 
        namestring = str(datetime.fromtimestamp(os.path.getctime(userdir + "/" + filename), timezone.utc))
        namestring = ''.join(e for e in namestring if e.isalnum())
        dst = namestring + str(i) + "tier" + tiertag + ".txt"
        src = userdir + "/" + filename
        dst = userdir + "/" + dst

        os.rename(src,dst)
        i += 1

if __name__ == '__main__':
    main()