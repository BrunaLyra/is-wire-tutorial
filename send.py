from is_wire.core import Channel, Message

# Connect to broker
channel = Channel("amqp://guest:guest@localhost:5672")

# Create a message
message = Message()
message.body = "Hello!".encode('latin1')

# Send message
channel.publish(message, topic="MyTopic.SubTopic")