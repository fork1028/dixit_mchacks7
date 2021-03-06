# Import socket module
import socket
import time
import pdb
class Client():

    msg_all_type = ['tell_story', 'choose_card_teller', 'choose_card_listener', 'broadcast_description',
                    'broadcast_cards', 'listener_guess']

    def __init__(self):
        # Create a socket object
        self.s = socket.socket()
        # Define the port on which you want to connect
        port = 12345
        # connect to the server on local computer
        self.s.connect(('192.168.1.1', port))
        self.s.send(str.encode('ready'))


# TODO: replace this with event, add id field of client
new_client = Client()

while True:
    output = str(new_client.s.recv(1024))
    if 'tellstory_request' in output:
        new_client.s.send(str.encode('tellstory_response 1 photo_description'))
    if 'choosecard_request' in output:
        # choosecard_response   int(playerId)   int(cardId)
        n = input('please, a number')
        new_client.s.send(str.encode('choosecard_response 1 {}'.format(n)))
    if output != 'b\'\'' and output != '':
        print(output)
    time.sleep(1)


# print('client received {}'.format(output))
# exit()
# output = output.split()
# if (output[0] == 'tell_story_instruct'):
#     new_client.s.send(str.encode('choose_card_teller 3'))
#     new_client.s.send(str.encode('tell_story content'))
# if(output[0] == 'broadcast_description'):
#     new_client.s.send(str.encode('choose_card_listener 1'))
# if(output[0] == 'broadcast_cards'):
#     new_client.s.send(str.encode('listener_guess 2'))
