Problem:
==============================================

The simplest example is client-server. Client sends "Hello" and server replies with "World".

Design
======

The recipe is divided to a client and server, client connects to the server and send a request, server binds and sending a reply.

Client uses a CLIENT socket type.
Server uses a SERVER socket type.

Clients steps:

1. Create a CLIENT socket
2. Connect to the server
3. Send "Hello" request message
4. Receive reply message

Server steps:

1. Create SERVER socket
2. Binds the socket
3. Receive request message
4. Send "World" reply message

Implementations:
===================
* [PyZMQ](https://github.com/zeromq/cookbook/blob/master/eventsourcing/code/pyzmq/)

References:
==============
* [GetEventStore](http://docs.geteventstore.com/introduction/event-sourcing-basics/)
* [Event Sourcing](http://www.martinfowler.com/eaaDev/EventSourcing.html)
