import asyncio
import sys

import structlog
from grpclib.health.check import ServiceStatus
from grpclib.health.service import Health
from grpclib.reflection.service import ServerReflection
from grpclib.server import Server
from module import Plugin
from stdio_service import GRPCStdioService

logger = structlog.get_logger()


async def serve() -> None:
    # Instantiate the plugin.
    plugin = Plugin()

    # Instantiate the stdio service.
    stdio = GRPCStdioService()

    # Create a health check for the plugin.
    plugin_health = ServiceStatus()
    plugin_health.set(True)
    health = Health({plugin: [plugin_health]})

    # Add reflection for the plugin and health check.
    services = ServerReflection.extend([plugin, stdio, health])

    # Instantiate the server.
    server = Server(services)

    # Start the server.
    await server.start("127.0.0.1", 50001)
    await server.wait_closed()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        # This is a special message that tells gatewayd to start the plugin.
        print("1|0|tcp|127.0.0.1:50001|grpc")
        sys.stdout.flush()
        asyncio.run(serve())
    except KeyboardInterrupt:
        pass
