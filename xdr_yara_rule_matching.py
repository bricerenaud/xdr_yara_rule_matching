# --- Yara rule matching script for Cortex XDR ---
# v0.1 - script creation (hruuttila@paloaltonetworks.com)
# v0.2 - "nice" and "ionice" settings, base85 encoding, Yara search options and "no match" message (brenaud@paloaltonetworks.com)

import os, gzip, base64, subprocess, psutil

# Yara64 v4.1.0 encoded in BASE85

def main(yararule,root_path):
	# Write Yara rules to disk
	frule = open('yararule.txt', 'w')
	frule.write(yararule)
	frule.close()

	# Write Yara Interpreter to disk
	with open('yara64.exe', 'wb') as f:
		f.write(gzip.decompress(base64.b85decode(ENCODED_YARA)))
	f.close()

	# Launch Yara search
	process = subprocess.Popen(['yara64.exe', '-frw', 'yararule.txt', root_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# Decrease process and IO priority to limit performance impact
	p = psutil.Process(process.pid)
	p.nice(psutil.IDLE_PRIORITY_CLASS)
	p.ionice(psutil.IOPRIO_VERYLOW)
    
	# Wait for the search to finish
	stdout, stderr = process.communicate()
    
	# Return a clean output
	if (stdout):
		raw_output = stdout.decode('utf-8')
		output = raw_output.splitlines()
	else:
		output = "No matching file found."
	
	# Delete everything from disk
	os.remove('yara64.exe')
	os.remove('yararule.txt')
    
	return(output)