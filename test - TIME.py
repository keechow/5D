import time

sys_time =  time.strftime("%c")
print sys_time
sy_time = sys_time.replace("/","")
s_time = sy_time.replace(":","")
_time = s_time.replace(" ", "_")
print _time
