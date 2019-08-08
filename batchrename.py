import os
import time
from datetime import datetime, timezone

def main():

    userDir = input("What subfolder are your files in?")
    tierTag = input("What tier tag would you like to add? (Leave empty if you don't need a tier system)")

    for filename in os.listdir(userDir): 

        fileExtension = filename.split(".")[-1]

        namestring = str(datetime.fromtimestamp(os.path.getctime(userDir + "/" + filename), timezone.utc))
        namestring = ''.join(e for e in namestring if e.isalnum())
        if tierTag:
            dst = namestring + "tier" + tierTag + "." + fileExtension
        else:
            dst = namestring + "." + fileExtension
        src = userDir + "/" + filename
        dst = userDir + "/" + dst

        os.rename(src,dst)

if __name__ == '__main__':
    main()