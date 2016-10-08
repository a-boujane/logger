import os
import time
momo=os.path.getatime("logger.py")
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(momo))