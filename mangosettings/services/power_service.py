from pathlib import Path
from gi.repository import Gio
class PowerService():
    def __init__(self):
        try:
            self.ppd = Gio.DBusProxy.new_for_bus_sync(Gio.BusType.SYSTEM, Gio.DBusProxyFlags.NONE,
                None, "org.freedesktop.UPower.PowerProfiles",
                "/org/freedesktop/UPower/PowerProfiles",
                "org.freedesktop.UPower.PowerProfiles", None)
        except:
            self.ppd = None

    def get_capacity(self):
        try:
            batteries = Path("/sys/class/power_supply").glob("BAT*/capacity")
            for battery in batteries:
                return int(battery.read_text().strip())
        except:
            return None
        return None
        
    def get_power_profile(self):
        if not self.ppd:
            return None
        profile = self.ppd.get_cached_property("ActiveProfile")
        if profile is None:
            return None
        return profile.unpack()