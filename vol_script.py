import os, os.path

def parse():
	workingD = """E:\Cases\
"""
	Files = []
	os.chdir(workingD)
	for root, dirs, files in os.walk(workingD, topdown = True):
		for name in files:
			filepath = os.path.join(root, name)
			Files.append({"name": name, "filepath": filepath})
	return Files

def get_profile():
	a = len
	vol = "py -2 vol.py imageinfo -f "
	for file_path in parse():
		command = vol + file_path['filepath']
		#profile_output = os.system(command + " | findstr 'Win*")		
		print(command + " >> C:\Users\emma\Desktop\Profiles.txt")

get_profile()


#py -2 C:\users\emma\volatility-master\volatility-master\vol.py imageinfo -f E:\Cases\a.dmp