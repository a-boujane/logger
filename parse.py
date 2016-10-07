import os
import re
import logger
import json
import time

timer= time.time()
def finalize(result):
    return "{"+result+"}"

# Create a new logger object
logger = logger.Logger();
# create the pattern for IPv4 addresses
pat = re.compile("\d+\.\d+\.\d+\.\d+")
# directory where logs are located
direct = "./logs/";

# Create a list containing all files in the logs dir
lissy = os.listdir(direct);


# iterate through the list of the files,
# and open only the ones containing .txt in them
#  and matching the regex predefined for the IP addresses
for filename in lissy:
    if(".txt" in filename):
        fil = open(direct+filename,'r')
        # Adding the address found to the logger's dictionnary
        logger.addItems(*pat.findall(fil.read()))
        fil.close()

result = logger.locate()

json.dumps(result)

print time.time()-timer
# finalize(result)

# print result


