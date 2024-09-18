# Standby and wake function.

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import  EntityCategory


from .const import DOMAIN
from .entity import AmbeoBaseSwitch

_LOGGER = logging.getLogger(__name__)

class Standby(AmbeoBaseSwitch):
    def __init__(self, device, api):
        """Initialize the Standby switch."""
        super().__init__(device, api, "Standby")

    async def async_turn_on(self):
        """Wake from standby."""
        await self.api.set_standby(False)
        self._is_on = False

    async def async_turn_off(self):
        """Sleep into standby."""
        await self.api.set_standby(True)
        self._is_on = True

    async def async_update(self):
        """Update the current status of standby."""
        try:
            status = await self.api.get_standby()
            self._is_on = status
        except Exception as e:
            _LOGGER.error(f"Failed to update standby status: {e}")

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities,
):
    """Set up the switch entities from a config entry created in the integrations UI."""
    ambeo_api = hass.data[DOMAIN][config_entry.entry_id]["api"]
    ambeo_device = hass.data[DOMAIN][config_entry.entry_id]["device"]
    entities = []
    if  ambeo_device.max_compat:
        entities.append(Standby(ambeo_device, ambeo_api))
    async_add_entities(entities, update_before_add=True)
