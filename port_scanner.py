#Import the socket library
import socket

#Specify that we want to use TCP with IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Set a timeout for the period of time for which the script will run before it returns
s.settimeout(5)

#Ask user to input the IP address that they want scanned, which can be saved as a string
host = input("Please enter the IP address you would like scanned: ")

#Ask user to input the port that they want scanned, which can be saved as an integer
port = int(input("Please enter the port you would like scanned: "))

#Allow the program to return an error message if the port is closed; otherwise declare that the port is open
def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed.")
        input("Press Enter to exit the script...")

    else:
        print("The port is open.")
        input("Press Enter to exit the script...")

portScanner(port)