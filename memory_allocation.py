import psutil
print(psutil.cpu_percent())
#How much diskspace is free?
import shutil
total, used, free = shutil.disk_usage('/')
print('Total:', total)
print('Used :', used)
print('Free :', free)
