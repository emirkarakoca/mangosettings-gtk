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
        return int(Path("/sys/class/power_supply/BAT0/capacity").read_text().strip())

    def get_power_profile(self):
        if not self.ppd:
            return None
        return self.ppd.get_cached_property("ActiveProfile").unpack()