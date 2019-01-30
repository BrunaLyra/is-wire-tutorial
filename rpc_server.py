from is_wire.core import Channel, StatusCode, Status
from is_wire.rpc import ServiceProvider, LogInterceptor
from google.protobuf.struct_pb2 import Struct
import time


def increment(struct, ctx):
    if struct.fields["value"].number_value < 0:
        # return error
        return Status(StatusCode.INVALID_ARGUMENT, "Number must be positive")

    time.sleep(0.2) # Simulate work
    struct.fields["value"].number_value += 1.0
    return struct


# Connect to broker
channel = Channel("amqp://guest:guest@localhost:5672")

#########Estudar este bloco!#########
provider = ServiceProvider(channel)
logging = LogInterceptor()
provider.add_interceptor(logging)

provider.delegate(
    topic="MyService.Increment",
    function=increment,
    request_type=Struct,
    reply_type=Struct)
####################################

provider.run() ## Process requests