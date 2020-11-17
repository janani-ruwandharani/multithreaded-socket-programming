import socket
import tqdm
import os
from _thread import *
import threading
import logging

# create the threading object
print_lock = threading.Lock()

# define thread function
def thread(client_socket):
    try:
        # receive 4096 bytes each time
        BUFFER_SIZE = 4096

        while True:
            # receive file info
            read_info = client_socket.recv(BUFFER_SIZE).decode()
            filename, filesize = read_info.split(",")

            # remove absolute path if there is
            filename = os.path.basename(filename)

            # start receiving file from the socket
            # writing to the file stream

            progress = tqdm.tqdm(range(int(filesize)), f'receiving {filename}', unit="B", unit_scale=True,
                                 unit_divisor=1024)

            with open(filename, "wb") as f:
                completed_amount = 0
                for _ in progress:
                    # receives 1024 bytes from the socket each time the loop runs
                    read_binary = client_socket.recv(BUFFER_SIZE)

                    if not read_binary:

                        print('File transferred successfully')
                        print_lock.release()
                        # lock released on exit
                        break
                        # nothing is received
                        # file transmitting is done

                    # write to the file the bytes just received
                    f.write(read_binary)

                    # update the progress bar
                    progress.update(len(read_binary))
                    completed_amount += len(read_binary)
                    completed_percentage = completed_amount*100/int(filesize)
                    if completed_percentage ==100:
                        print('Completion percentage: {}'.format(str(completed_percentage)))
            break

        # close the client
        client_socket.close()

    except Exception as e:
        import traceback
        logging.error(e)
        print(' ')


def Main():
    try:
        # create the server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # assign the host ip
        server_host = '0.0.0.0'

        # assign the port
        server_port = 1234

        local_ip = socket.getfqdn()

        # bind the socket
        server_socket.bind((server_host, server_port))

        # put the server on the listening mode
        server_socket.listen(5)
        print(f'Server is listening on {server_port} at {local_ip}')

        # forever loop until client wants to exit
        while True:
            # connect to the client
            client_socket, address = server_socket.accept()

            # client acquires the lock
            print_lock.acquire()
            print(f' Got connection from {address} ')

            # start a new thread and return its identifier
            start_new_thread(thread, (client_socket,))

        # close the server
        server_socket.close()

    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    Main()





