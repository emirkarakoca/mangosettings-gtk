import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from ..services.audio_service import AudioService

def build():
    audio = AudioService()
    sinks = audio.get_sinks()
    if not sinks:
        return  #logger
    
    page = Adw.PreferencesPage(title="Ses")
    
    output = Adw.PreferencesGroup(title="Çıkış")

    device_combo = Adw.ComboRow(title="Çıkış Aygıtı")  #expander row denicem
    device_combo.set_model(Gtk.StringList.new([sink["name"] for sink in sinks]))
    default_index = 0
    for index, sink in enumerate(sinks):
        if sink["default"]:
            default_index = index
            break
    device_combo.set_selected(default_index)

    volume_row = Adw.ActionRow(title="Ses")
    value_label = Gtk.Label(label=f"%{int(audio.get_volume())}")
    value_label.set_width_chars(4)
    scale = Gtk.Scale.new_with_range(orientation=Gtk.Orientation.HORIZONTAL, min=0, max=100, step=1)    
    scale.set_value(audio.get_volume())
    scale.set_hexpand(True)
    volume_row.add_suffix(value_label)
    volume_row.add_suffix(scale)
    volume_row.set_activatable(False)

    mute_row = Adw.SwitchRow(title="Sessize Al")
    mute_row.set_active(audio.get_mute())

    def on_volume_changed(slider):
        value = slider.get_value()
        audio.set_volume(value)
        value_label.set_text(f"%{int(value)}")
        
    def change_device(row, _):
        audio.set_default_sink(sinks[row.get_selected()]["id"])
        scale.set_value(audio.get_volume())
        mute_row.set_active(audio.get_mute())     

    device_combo.connect("notify::selected", change_device)
    scale.connect("value-changed", on_volume_changed)  
    mute_row.connect("notify::active", lambda row, _: audio.set_mute(row.get_active()))
    
    output.add(device_combo)
    output.add(volume_row)
    output.add(mute_row)
    page.add(output)    
    return page