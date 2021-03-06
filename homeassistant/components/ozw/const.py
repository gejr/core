"""Constants for the ozw integration."""
from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR_DOMAIN
from homeassistant.components.climate import DOMAIN as CLIMATE_DOMAIN
from homeassistant.components.cover import DOMAIN as COVER_DOMAIN
from homeassistant.components.fan import DOMAIN as FAN_DOMAIN
from homeassistant.components.light import DOMAIN as LIGHT_DOMAIN
from homeassistant.components.lock import DOMAIN as LOCK_DOMAIN
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN

DOMAIN = "ozw"
DATA_UNSUBSCRIBE = "unsubscribe"
PLATFORMS = [
    BINARY_SENSOR_DOMAIN,
    COVER_DOMAIN,
    CLIMATE_DOMAIN,
    FAN_DOMAIN,
    LIGHT_DOMAIN,
    LOCK_DOMAIN,
    SENSOR_DOMAIN,
    SWITCH_DOMAIN,
]
MANAGER = "manager"
OPTIONS = "options"

# MQTT Topics
TOPIC_OPENZWAVE = "OpenZWave"

# Common Attributes
ATTR_CONFIG_PARAMETER = "parameter"
ATTR_CONFIG_VALUE = "value"
ATTR_INSTANCE_ID = "instance_id"
ATTR_SECURE = "secure"
ATTR_NODE_ID = "node_id"
ATTR_SCENE_ID = "scene_id"
ATTR_SCENE_LABEL = "scene_label"
ATTR_SCENE_VALUE_ID = "scene_value_id"
ATTR_SCENE_VALUE_LABEL = "scene_value_label"

# Service specific
SERVICE_ADD_NODE = "add_node"
SERVICE_REMOVE_NODE = "remove_node"
SERVICE_SET_CONFIG_PARAMETER = "set_config_parameter"

# Home Assistant Events
EVENT_SCENE_ACTIVATED = f"{DOMAIN}.scene_activated"

# Signals
SIGNAL_DELETE_ENTITY = f"{DOMAIN}_delete_entity"

# Discovery Information
DISC_COMMAND_CLASS = "command_class"
DISC_COMPONENT = "component"
DISC_GENERIC_DEVICE_CLASS = "generic_device_class"
DISC_GENRE = "genre"
DISC_INDEX = "index"
DISC_INSTANCE = "instance"
DISC_NODE_ID = "node_id"
DISC_OPTIONAL = "optional"
DISC_PRIMARY = "primary"
DISC_SPECIFIC_DEVICE_CLASS = "specific_device_class"
DISC_TYPE = "type"
DISC_VALUES = "values"
