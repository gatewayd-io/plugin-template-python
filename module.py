import structlog
from google.protobuf.json_format import MessageToDict
from google.protobuf.struct_pb2 import ListValue, Struct, Value
from grpclib.server import Stream

from plugin.v1.plugin_grpc import GatewayDPluginServiceBase
from mapping import MappingMixin

logger = structlog.get_logger()


async def defaults(stream: Stream[Struct, Struct]) -> None:
    """Default handler for all hooks.

    Note:
        The GatewayDPluginServiceBase class implements all hooks as abstract
        methods, so we need to implement them all. This is a default handler
        to use for all hooks that we don't need to implement.
    """
    req = await stream.recv_message()
    if req:
        await stream.send_message(req)
    else:
        await stream.send_message(Struct())


class Plugin(MappingMixin, GatewayDPluginServiceBase):
    async def GetPluginConfig(self, stream: Stream[Struct, Struct]) -> None:
        # Ignore the request, as it is empty.
        await stream.recv_message()
        await stream.send_message(
            Struct(
                fields={
                    "id": Value(
                        struct_value=Struct(
                            fields={
                                "name": Value(string_value="plugin-template-python"),
                                "version": Value(string_value="0.1.0"),
                                "remoteUrl": Value(
                                    string_value="github.com/gatewayd-io/plugin-template-python"
                                ),
                            }
                        )
                    ),
                    "hooks": Value(
                        list_value=ListValue(
                            values=[
                                # The list of hooks that the plugin implements.
                                Value(number_value=16),  # OnTrafficFromClient
                            ]
                        )
                    ),
                }
            )
        )

    async def OnBooted(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnBooting(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnClosed(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnClosing(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnConfigLoaded(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnHook(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnNewClient(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnNewLogger(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnNewPool(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnNewProxy(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnNewServer(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnOpened(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnOpening(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnRun(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnShutdown(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnSignal(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnTick(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnTraffic(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnTrafficFromClient(self, stream: Stream[Struct, Struct]) -> None:
        """
        This is an example of how to use the OnTrafficFromClient hook to
        intercept traffic from the client and modify it before it is sent to
        the server. In this example, we simply log the request and send it
        to the server.
        """
        req = await stream.recv_message()
        if req:
            logger.info(MessageToDict(req))
            await stream.send_message(req)
        else:
            await stream.send_message(Struct())

    async def OnTrafficFromServer(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnTrafficToClient(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnTrafficToServer(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)
