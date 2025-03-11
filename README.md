# Overview

This is a simple chat program that allows users on other devices to communicate through text across a server. You need to start up the server before running any client programs otherwise the client won't know what to connect to. Once the server is up and running you can start up the client program. You will be prompted for a username to identify your messages and then you can start typing and sending messages. If you wish to quit the program simply type 'exit' and confirm you want to quit by typing either 'y' or 'yes'. This will end the client program. To end the server program simply kill/close the application. (Note: if you close the server before closing client programs the client programs will turn to a blank screen and need to be killed/closed like the server.)


I'm pretty fluent with Python but I've never created software that's designed to communicate with other devices. I wanted to take this opportunity to further my skills and abilities with Python and coding. Through this project I learned some basics of network communication through Python and how I can apply that knowledge and my skills in the future. I want to push my knowledge and abilities further, so this software is a stepping stone in that direction.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/t8MhCu1l-nM)

# Network Communication

I created a server that runs on a device and connects to a HOST IP and a PORT on a network. It then allows other users to connect to the server by running the same HOST IP and PORT.

This software uses TCP for its network communication.

The format of messages is simple text being sent to the server and relayed to all connected clients.

# Development Environment

I used ChatGPT to help me create a tutorial which helped me understand how to impliment the server sockets and threads. I then used many forums and other websites to help troubleshoot and fine tune the code to work more seamlessly between the clients and the server.

I used Python programming language and the 'os', 'socket', 'serversocket', and 'threading' libraries.

# Useful Websites

* [ChatGPT](https://chatgpt.com/)
* [socketserver — A framework for network servers](https://docs.python.org/3/library/socketserver.html)
* [Geeks for Geeks — Multithreading in Python](https://www.geeksforgeeks.org/multithreading-python-set-1/)

# Future Work

* Work on bettering the network communication.
* Find a way to shutdown the server internally instead of killing the program.
* Create a GUI to make the chat easier to read and work with.