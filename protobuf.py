from is_wire.core import Channel, Subscription, Message, ContentType
from google.protobuf.struct_pb2 import Struct

# Connect to broker
channel = Channel("amqp://guest:guest@localhost:5672")


## Subscribe
subscription = Subscription(channel)
subscription.subscribe(topic="MyTopic.SubTopic")


# Create struct
struct = Struct()
struct.fields["apples"].string_value = "red"

# Create message
message = Message()
message.content_type = ContentType.JSON
message.pack(struct) # Serialize struct

channel.publish(message, topic="MyTopic.SubTopic")


## Receive message
received_message = channel.consume()
received_struct = received_message.unpack(Struct)


### Check if they are equal
assert struct == received_struct
