import socket
import tqdm
import os

# buffer size
BUFFER_SIZE = 4096

# create the socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ip address of the server we need to connect to
host = '192.168.1.9'
# server port we need to connect to
port = 1234

#name of the file we want to send
filename ='song 2.mp3'

# get the size of the file
filesize = os.path.getsize(filename)

# connect the socket to the server
s.connect((host,port))
print(f"Connected to the server at {port} and {host}")

# send the filename and size
s.send(f'{filename},{filesize}'.encode())

# start sending file
progress = tqdm.tqdm(range(filesize), f'sending {filename}', unit="B", unit_scale = True, unit_divisor = 1024)

with open(filename, "rb") as f:
    for _ in progress:
        # read 1024 bytes form the file each time the loop runs
        read_file = f.read(BUFFER_SIZE)

        if not read_file:
            break
            # file transmitting is done

        # use sendall to send file in busy network
        s.sendall(read_file)

        # update the progress bar
        progress.update(len(read_file))


server_name = socket.gethostbyaddr(host)
print(f'file successfully sent to {server_name}')


# close the socket
s.close()
