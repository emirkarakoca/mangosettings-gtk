import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from ..services.power_service import PowerService

def build(_):
    ps = PowerService()
    page = Adw.PreferencesPage(title="Güç")
    blevel_group = Adw.PreferencesGroup(title="Pil Düzeyi")
    bbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    capacity = ps.get_capacity()
    if capacity is None:
        bpercent = Gtk.Label(label="Pil Bulunamadı")
        bbox.append(bpercent)
    else:
        bpercent = Gtk.Label(label=f"{capacity}%")
        bpercent.set_halign(Gtk.Align.END)
        bbox.append(bpercent)
        blevel_bar = Gtk.ProgressBar()
        blevel_bar.set_fraction(capacity/100.0)
        bbox.append(blevel_bar)
    blevel_group.add(bbox)

    page.add(blevel_group)
    return page