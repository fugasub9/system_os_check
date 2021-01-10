import sys
import os
import re

system_os = sys.platform
user_home_path = os.environ['HOME']
wsl2_path_pattern = "^\/mnt\/"
#print(wsl2_path_pattern)

print(system_os)
print(user_home_path)

if(system_os == "linux"):
	if(re.match(wsl2_path_pattern, user_home_path)):
		#print(re.match(wsl2_path_pattern, os.environ['HOME']))
		print('wsl2 of Windows OS')
	else:
		#print(re.match(wsl2_path_pattern, os.environ['HOME']))
		print('other Linux OS')

elif(system_os == "darwin"):
	print('Mac OS')
