import subprocess
import os

out = subprocess.check_output("xinput | grep 'Synaptics' | awk '{print $6}'", shell = True).strip()

synapticId = out.replace('id=', '')

getPropsOut = subprocess.check_output("xinput list-props " +
	synapticId + " | grep '143' | awk '{print $4}'", shell = True).strip()

newCmd = ''

if getPropsOut == '1':
	newCmd = "xinput disable " + synapticId

elif getPropsOut == '0':
	newCmd = "xinput enable " + synapticId

else:
	print "Else triggered"

os.system(newCmd)