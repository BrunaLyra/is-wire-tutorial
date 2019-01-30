from __future__ import print_function
from is_wire.core import Channel, Subscription

# Connect to broker
channel = Channel("amqp://guest:guest@localhost:5672")

# Subscribe
subscription = Subscription(channel)
subscription.subscribe(topic="MyTopic.SubTopic")

# Wait for a message
message = channel.consume()
print(message.body)