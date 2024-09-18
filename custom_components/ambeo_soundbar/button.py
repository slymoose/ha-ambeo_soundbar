from homeassistant.components.button import ButtonDeviceClass, ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import  EntityCategory
from .entity import AmbeoBaseEntity
from .const import DOMAIN



class AmbeoReboot(AmbeoBaseEntity, ButtonEntity):
    """The class remains largely unchanged."""
    def __init__(self, device, api):
        """Initialize the switch entity."""
        super().__init__(device, api, "Ambeo Reboot", "ambeo_reboot")

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.api.reboot();    
            
    @property
    def entity_category(self) -> EntityCategory:
        """Return the entity category."""
        return EntityCategory.CONFIG

    @property
    def device_class(self) -> ButtonDeviceClass:
        """Return the device class."""
        return ButtonDeviceClass.RESTART


class AmbeoWake(AmbeoBaseEntity, ButtonEntity):
    """Wakes up the Ambeo."""
    def __init__(self, device, api):
        """Initialize the switch entity."""
        super().__init__(device, api, "Ambeo Wake", "ambeo_wake")

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.api.wake();

    @property
    def entity_category(self) -> EntityCategory:
        """Return the entity category."""
        return EntityCategory.CONFIG

    @property
    def device_class(self) -> ButtonDeviceClass:
        """Return the device class."""
        return ButtonDeviceClass.RESTART

class AmbeoStandby(AmbeoBaseEntity, ButtonEntity):
    """Staby mode for the Ambeo."""
    def __init__(self, device, api):
        """Initialize the switch entity."""
        super().__init__(device, api, "Ambeo Standby", "ambeo_standby")

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.api.stand_by();

    @property
    def entity_category(self) -> EntityCategory:
        """Return the entity category."""
        return EntityCategory.CONFIG

    @property
    def device_class(self) -> ButtonDeviceClass:
        """Return the device class."""
        return ButtonDeviceClass.RESTART
    
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities,
):
    """Set up the switch entities from a config entry created in the integrations UI."""
    ambeo_api = hass.data[DOMAIN][config_entry.entry_id]["api"]
    ambeo_device = hass.data[DOMAIN][config_entry.entry_id]["device"]
     entities = []
    entities.append(AmbeoReboot(ambeo_device, ambeo_api))
    entities.append(AmbeoWake(ambeo_device, ambeo_api))
    entities.append(AmbeoStandby(ambeo_device, ambeo_api))
    async_add_entities(entities) #may need (entities, update_before_add=True)
    async_add_entities(entities)
