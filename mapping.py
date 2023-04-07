import typing
import grpclib


class MappingMixin:
    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        """Mapping of service methods to handlers.

        Note:
            This method is used to remap the service name to the plugin name,
            so that the plugin health check works properly.
        """
        # Get the mapping from the base class
        mapping = super().__mapping__()  # type: ignore
        remapping = {}

        # Replace the service name with the plugin name
        for path in mapping:
            repath = path.replace("plugin.v1.GatewayDPluginService", "plugin")
            remapping[repath] = mapping[path]

        # Merge the two mappings
        remapping.update(mapping)

        return remapping
