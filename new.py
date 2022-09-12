import subprocess

cmd = 'ls -lah /'
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()
return_value = process.returncode
print(output)
