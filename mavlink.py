import threading
import time
import sys
import datetime
from Constant import Server,CommandConstant,User,ProjectConstant
from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = Server.ServerClass.get_server_secret_key()
socketio = SocketIO(app)
from socketIO_client import SocketIO as client_socketio, BaseNamespace
import json
def init_sender_socket():
    global my_client_send
    my_client_send = client_socketio(ProjectConstant.ProjectConstantClass.get_host(),ProjectConstant.ProjectConstantClass.get_port())
def send_message(send_msg):
    my_client_send.emit('chat message', send_msg)
#BATTERY INFO
def init_socket():
    my_client = client_socketio(Server.ServerClass.get_server_ip(), Server.ServerClass.get_server_port())
    @socketio.on('chat message')
    def handle_message(message):
        print('received message init: ' + message)

    def socket_receiver(data):
        try:
            print (data)
            #vehicle = mpstate.get_vehicles()[0]
            #obj_data = json.loads(data.replace('\r\n', '\\r\\n'),strict=False)
            #obj_data = json.loads(data,strict=False)
            #obj_data = json.loads(data)
            #sender_user = obj_data['u']
            
        except Exception as error:
            print (error)
        #set_command(data)
    my_client.on('chat message', socket_receiver)
    my_client.wait()
#{"action":"wp","data":""}
if __name__ == '__main__':
    
    thread_receiver = threading.Thread(target=init_socket)
    thread_receiver.daemon = True
    thread_receiver.start()
    
    thread_sender = threading.Thread(target=init_sender_socket)
    thread_sender.daemon = True
    thread_sender.start()
    socketio.run(app)


