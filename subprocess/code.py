"""
The subprocess module allows you to spawn new processes, connect to their 
input/output/error pipes, and obtain their return codes. This module intends to replace 
several older modules and functions:

"""
import subprocess

# subprocess.run("ls")
# p1 = subprocess.run(["ls", "-la"])
# p2 = subprocess.run(["ls", "-la"], capture_output=True)

# To convert the raw bytes to String directly
# p3 = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE, text=True)

# To
# with open("output.txt", "w") as f:
#     p3 = subprocess.run(["ls", "-la"], stdout=f, text=True)

# p4 = subprocess.run(["ls", "-la", "dne"], stderr=subprocess.DEVNULL)
p4 = subprocess.run(["cat", "test_file.txt"], capture_output=True, text=True)
print(p4.stdout)

# print(p1)
# print(p1.args[1])
# print(p1.returncode)
# print(p2.stdout.decode())  # decode converts it to String
