from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
 
   # Create socket called clientSocket and establish a TCP connection with mailserver and port

   # Fill in start
   # Fill in end
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver,port))
   
   recv = clientSocket.recv(1024).decode()
   print(recv)
   if recv[:3] != '220':
       print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   # Fill in start
   # Fill in end
   mailFrom = "<mr6439@nyu.edu>\r\n"
   clientSocket.send(mailFrom.encode())
   recv2 = clientSocket.recv(1024)
   print(recv2)
   if recv2[:3] != "250":
      print('250 reply not received from server.')

   # Send RCPT TO command and print server response.
   # Fill in start
   # Fill in end
   rcptTo = "<mohanraghu@gmail.com>\r\n"
   clientSocket.send(rcptTo.encode())
   recv3 = clientSocket.recv(1024)
   print(recv3)
   if recv3[:3] != "250":
      print('250 reply not received from server.')

   # Send DATA command and print server response.
   # Fill in start
   # Fill in end
   data = "DATA\r\n"
   clientSocket.send(data.encode())
   recv4 = clientSocket.recv(1024)
   print(recv4)
   if recv4[:3] != "354":
      print('354 reply not received from server.')
     

   # Send message data.
   # Fill in start
   # Fill in end
   message = "\r\n.\r\n"
   clientSocket.send(message.encode())

   # Message ends with a single period.
   # Fill in start
   # Fill in end
   endmsg = "\r\n.\r\n"
   clientSocket.send(endmsg.encode())

   # Send QUIT command and get server response.
   # Fill in start
   # Fill in end
  quitCommand = 'QUIT\r\n'
  clientSocket.send(quitCommand.encode())
  recv5 = clientSocket.recv(1024).decode()
  print(recv5)
  clientSocket.close()


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
