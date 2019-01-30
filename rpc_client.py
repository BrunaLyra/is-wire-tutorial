from __future__ import print_function
from is_wire.core import Channel, Message, Subscription
from google.protobuf.struct_pb2 import Struct
import socket

# Connect to broker
channel = Channel("amqp://guest:guest@localhost:5672")

subscription = Subscription(channel)
struct = Struct()
struct.fields["value"].number_value = 1.0

# Make request
request = Message(content=struct, reply_to=subscription)
channel.publish(request, topic="MyService.Increment")

# Wait for reply
try:
    reply = channel.consume(timeout = 1.0)
    struct = reply.unpack(Struct)
    print('RPC Status:', reply.status, '\nReply', struct)
except socket.timeout:
    print('No reply')