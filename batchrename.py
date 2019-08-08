import os
import time
from datetime import datetime, timezone

def main():
    #i = 0 #comment out this feature when not used in testing

    userDir = input("What subfolder are your files in?")
    tierTag = input("What tier tag would you like to add? (Specific to Dev's needs)")
    #add custom file extensions by stripping last text from filename before the period

    for filename in os.listdir(userDir): 
        namestring = str(datetime.fromtimestamp(os.path.getctime(userDir + "/" + filename), timezone.utc))
        namestring = ''.join(e for e in namestring if e.isalnum())
        if tierTag:
            dst = namestring + str(i) + "tier" + tierTag + ".txt"
        else:
            dst = namestring + str(i) + "tier" + ".txt"
        src = userDir + "/" + filename
        dst = userDir + "/" + dst

        os.rename(src,dst)
        #i += 1

if __name__ == '__main__':
    main()