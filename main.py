import subprocess

print("Which server do you want to run?")
print("1. Single threaded")
print("2. Multi threaded")
s_opt = input("Enter your choice: ")
if s_opt=="1":
    subprocess.call('start python server1.py', shell=True, cwd="./xmlrpc-single-thread")
    subprocess.call('start python server2.py', shell=True, cwd="./xmlrpc-single-thread")
    subprocess.call('start python server3.py', shell=True, cwd="./xmlrpc-single-thread")
elif s_opt=="2":
    subprocess.call('start python server.py', shell=True, cwd="./xmlrpc-multi-thread")

print("Which client do you want to run?")
print("1. Single threaded")
print("2. Multi threaded")
c_opt = input("Enter your choice: ")
if c_opt=="1":
    subprocess.call('python client.py', shell=True, cwd="./xmlrpc-single-thread")
elif c_opt=="2":
    subprocess.call('python client.py', shell=True, cwd="./xmlrpc-multi-thread")
