# multithreaded-socket-programming
Transfer files between two machines while displaying the transferred percentage in a progress bar

Description:
This project can transfer files between two machines when the firewall is disabled. The transferring percentage is displayed through a progress bar. However, the multithreading feature needs to be improved more.
Based on https://www.geeksforgeeks.org/socket-programming-multi-threading-python/ and https://www.thepythoncode.com/article/send-receive-files-using-sockets-python

Installation:
1. Install the requirements.txt file with 'pip install -r requirements.txt'
2. Turn off the firewall on both machines and run the 'server.py' first
3. Then run 'client.py'
4. Try for more than one client scripts to experience mutithreading

Results:
On server side
1. single client

