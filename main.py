import sys
import asyncio
import typing
from plugin.v1.plugin_grpc import GatewayDPluginServiceBase
from google.protobuf.struct_pb2 import ListValue, Struct, Value
from google.protobuf.json_format import MessageToDict
import grpclib
from grpclib.server import Server, Stream
from grpclib.reflection.service import ServerReflection
from grpclib.health.service import Health
from grpclib.health.check import ServiceStatus
import logging

logging.basicConfig(filename="plugin.log", level=logging.INFO)


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


class Plugin(GatewayDPluginServiceBase):
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
            logging.info(MessageToDict(req))
            await stream.send_message(req)
        else:
            await stream.send_message(Struct())

    async def OnTrafficFromServer(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnTrafficToClient(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    async def OnTrafficToServer(self, stream: Stream[Struct, Struct]) -> None:
        await defaults(stream)

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        """Mapping of service methods to handlers.

        Note:
            This method is used to remap the service name to the plugin name,
            so that the plugin health check works properly.
        """
        # Get the mapping from the base class
        mapping = super().__mapping__()
        remapping = {}

        # Replace the service name with the plugin name
        for path in mapping:
            repath = path.replace("plugin.v1.GatewayDPluginService", "plugin")
            remapping[repath] = mapping[path]

        # Merge the two mappings
        remapping.update(mapping)

        return remapping


async def serve() -> None:
    # Instantiate the plugin.
    plugin = Plugin()

    # Create a health check for the plugin.
    plugin_health = ServiceStatus()
    plugin_health.set(True)
    health = Health({plugin: [plugin_health]})

    # Add reflection for the plugin and health check.
    services = ServerReflection.extend([plugin, health])

    # Instantiate the server.
    server = Server(services)

    # Start the server.
    await server.start("127.0.0.1", 12345)
    await server.wait_closed()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        # This is a special message that tells gatewayd to start the plugin.
        print("1|0|tcp|127.0.0.1:12345|grpc")
        sys.stdout.flush()
        asyncio.run(serve())
    except KeyboardInterrupt:
        pass
