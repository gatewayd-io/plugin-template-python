from typing import Type
from plugin.v1.grpc_stdio_grpc import GRPCStdioBase
from grpclib.server import Stream
from plugin.v1.grpc_stdio_pb2 import DESCRIPTOR
from google.protobuf.empty_pb2 import Empty

StdioData = DESCRIPTOR.message_types_by_name["StdioData"]._concrete_class
StdioDataType = Type[StdioData]


class GRPCStdioService(GRPCStdioBase):
    async def StreamStdio(self, stream: Stream[Empty, StdioDataType]) -> None:
        # Send the request back
        await stream.send_message(StdioData(
            channel=1,
            data=b"Hello World",
        ))
