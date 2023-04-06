# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugin/v1/plugin.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16plugin/v1/plugin.proto\x12\tplugin.v1\x1a\x1cgoogle/protobuf/struct.proto"s\n\x08PluginID\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x1d\n\nremote_url\x18\x03 \x01(\tR\tremoteUrl\x12\x1a\n\x08\x63hecksum\x18\x04 \x01(\tR\x08\x63hecksum"\x81\x04\n\x0cPluginConfig\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x13.plugin.v1.PluginIDR\x02id\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x18\n\x07\x61uthors\x18\x03 \x03(\tR\x07\x61uthors\x12\x18\n\x07license\x18\x04 \x01(\tR\x07license\x12\x1f\n\x0bproject_url\x18\x05 \x01(\tR\nprojectUrl\x12;\n\x06\x63onfig\x18\x06 \x03(\x0b\x32#.plugin.v1.PluginConfig.ConfigEntryR\x06\x63onfig\x12)\n\x05hooks\x18\x07 \x03(\x0e\x32\x13.plugin.v1.HookNameR\x05hooks\x12\x41\n\x08requires\x18\x08 \x03(\x0b\x32%.plugin.v1.PluginConfig.RequiresEntryR\x08requires\x12\x12\n\x04tags\x18\t \x03(\tR\x04tags\x12\x1e\n\ncategories\x18\n \x03(\tR\ncategories\x1a\x39\n\x0b\x43onfigEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a;\n\rRequiresEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01*\x92\x05\n\x08HookName\x12\x19\n\x15HOOK_NAME_UNSPECIFIED\x10\x00\x12\x1e\n\x1aHOOK_NAME_ON_CONFIG_LOADED\x10\x01\x12\x1b\n\x17HOOK_NAME_ON_NEW_LOGGER\x10\x02\x12\x19\n\x15HOOK_NAME_ON_NEW_POOL\x10\x03\x12\x1b\n\x17HOOK_NAME_ON_NEW_CLIENT\x10\x04\x12\x1a\n\x16HOOK_NAME_ON_NEW_PROXY\x10\x05\x12\x1b\n\x17HOOK_NAME_ON_NEW_SERVER\x10\x06\x12\x17\n\x13HOOK_NAME_ON_SIGNAL\x10\x07\x12\x14\n\x10HOOK_NAME_ON_RUN\x10\x08\x12\x18\n\x14HOOK_NAME_ON_BOOTING\x10\t\x12\x17\n\x13HOOK_NAME_ON_BOOTED\x10\n\x12\x18\n\x14HOOK_NAME_ON_OPENING\x10\x0b\x12\x17\n\x13HOOK_NAME_ON_OPENED\x10\x0c\x12\x18\n\x14HOOK_NAME_ON_CLOSING\x10\r\x12\x17\n\x13HOOK_NAME_ON_CLOSED\x10\x0e\x12\x18\n\x14HOOK_NAME_ON_TRAFFIC\x10\x0f\x12$\n HOOK_NAME_ON_TRAFFIC_FROM_CLIENT\x10\x10\x12"\n\x1eHOOK_NAME_ON_TRAFFIC_TO_SERVER\x10\x11\x12$\n HOOK_NAME_ON_TRAFFIC_FROM_SERVER\x10\x12\x12"\n\x1eHOOK_NAME_ON_TRAFFIC_TO_CLIENT\x10\x13\x12\x19\n\x15HOOK_NAME_ON_SHUTDOWN\x10\x14\x12\x15\n\x11HOOK_NAME_ON_TICK\x10\x15\x12\x15\n\x11HOOK_NAME_ON_HOOK\x10\x16\x32\xe9\x0b\n\x15GatewayDPluginService\x12\x43\n\x0fGetPluginConfig\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12\x42\n\x0eOnConfigLoaded\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12?\n\x0bOnNewLogger\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12=\n\tOnNewPool\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12?\n\x0bOnNewClient\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12>\n\nOnNewProxy\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12?\n\x0bOnNewServer\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12<\n\x08OnSignal\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12\x39\n\x05OnRun\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12=\n\tOnBooting\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12<\n\x08OnBooted\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12=\n\tOnOpening\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12<\n\x08OnOpened\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12=\n\tOnClosing\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12<\n\x08OnClosed\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12=\n\tOnTraffic\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12G\n\x13OnTrafficFromClient\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12\x45\n\x11OnTrafficToServer\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12G\n\x13OnTrafficFromServer\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12\x45\n\x11OnTrafficToClient\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12>\n\nOnShutdown\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12:\n\x06OnTick\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\x12:\n\x06OnHook\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.StructB6Z4github.com/gatewayd-io/gatewayd-plugin-sdk/plugin/v1b\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "plugin.v1.plugin_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"Z4github.com/gatewayd-io/gatewayd-plugin-sdk/plugin/v1"
    )
    _PLUGINCONFIG_CONFIGENTRY._options = None
    _PLUGINCONFIG_CONFIGENTRY._serialized_options = b"8\001"
    _PLUGINCONFIG_REQUIRESENTRY._options = None
    _PLUGINCONFIG_REQUIRESENTRY._serialized_options = b"8\001"
    _HOOKNAME._serialized_start = 701
    _HOOKNAME._serialized_end = 1359
    _PLUGINID._serialized_start = 67
    _PLUGINID._serialized_end = 182
    _PLUGINCONFIG._serialized_start = 185
    _PLUGINCONFIG._serialized_end = 698
    _PLUGINCONFIG_CONFIGENTRY._serialized_start = 580
    _PLUGINCONFIG_CONFIGENTRY._serialized_end = 637
    _PLUGINCONFIG_REQUIRESENTRY._serialized_start = 639
    _PLUGINCONFIG_REQUIRESENTRY._serialized_end = 698
    _GATEWAYDPLUGINSERVICE._serialized_start = 1362
    _GATEWAYDPLUGINSERVICE._serialized_end = 2875
# @@protoc_insertion_point(module_scope)
