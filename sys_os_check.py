import sys
import os
import re

tech_name = os.name
system_os = sys.platform
os_info = tech_name + " " + system_os
user_home_path = os.environ['HOME']
wsl2_path_pattern = "^\/mnt\/"

#print(system_os)
print(os_info)
print(user_home_path)

if(system_os == "linux" or system_os == "linux2"):
	if(re.match(wsl2_path_pattern, user_home_path)):
		print('wsl2 of Windows OS')
	else:
		print('other Linux OS')

elif(system_os == "darwin"):
	print('Mac OS')
