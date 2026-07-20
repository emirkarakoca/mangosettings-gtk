import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gdk
import subprocess
def create_switch(item, manager):
    switch = Adw.SwitchRow(title=item["label"], subtitle=item.get("subtitle", ""))
    switch.set_active(manager.get_bool(item["key"],item["default"]))
    switch.connect("notify::active",lambda s, _: manager.set(item["key"], s.get_active()))
    return switch

def create_spin(item, manager):
    if item["type"] == "int":
        value = manager.get_int(item["key"], item["default"])
    else:
        value = manager.get_float(item["key"], item["default"])
    adjustment = Gtk.Adjustment(lower=item["min"],upper=item["max"],
    step_increment=item["step"],value=value)
    spin = Adw.SpinRow(title=item["label"], subtitle=item.get("subtitle", ""), adjustment=adjustment)
    if "digits" in item:
        spin.set_digits(item["digits"])
    spin.connect("notify::value", lambda s, _: manager.set(item["key"], int(s.get_value()) if item["type"] == "int" else s.get_value()))
    return spin

def create_combo(item,manager):
    combo = Adw.ComboRow(title=item["label"], subtitle=item.get("subtitle", ""))

    model = Gtk.StringList()
    for option in item["options"]:
        model.append(option["label"])
    combo.set_model(model)

    current = manager.get(item["key"])
    if current is None:
        current = item["default"]
    selected = 0

    for index, option in enumerate(item["options"]):
        if str(option["value"]) == str(current):
            selected = index
            break
    combo.set_selected(selected)

    def changed(combo, pspec):
        index = combo.get_selected()
        value = item["options"][index]["value"]
        manager.set(item["key"],value)

    combo.connect("notify::selected",changed)
    return combo
    
def hex_to_rgba(value):
    value = value.replace("0x", "")

    if len(value) != 8:
        return Gdk.RGBA()

    rgba = Gdk.RGBA()

    rgba.red = int(value[0:2], 16) / 255
    rgba.green = int(value[2:4], 16) / 255
    rgba.blue = int(value[4:6], 16) / 255
    rgba.alpha = int(value[6:8], 16) / 255

    return rgba


def rgba_to_hex(rgba):
    return (
        f"0x"
        f"{round(rgba.red * 255):02x}"
        f"{round(rgba.green * 255):02x}"
        f"{round(rgba.blue * 255):02x}"
        f"{round(rgba.alpha * 255):02x}"
    )

def create_color(item, manager):
    row = Adw.ActionRow(title=item["label"], subtitle=item.get("subtitle", ""))
    current = manager.get(item["key"])
    if current is None:
        current = item["default"]

    rgba = hex_to_rgba(current)

    dialog = Gtk.ColorDialog()
    button = Gtk.ColorDialogButton(dialog=dialog)
    button.set_rgba(rgba)
    def changed(button, _):
        color = button.get_rgba()
        manager.set(item["key"], rgba_to_hex(color))
        subprocess.run(["mmsg","dispatch","reload_config"],check=False)
    button.connect("notify::rgba", changed)

    row.add_suffix(button)
    return row

ROW_BUILDERS = {"bool": create_switch, "int": create_spin, "float": create_spin, "choice": create_combo, "color": create_color}

def create_row(item, manager):
    builder = ROW_BUILDERS.get(item["type"])
    if builder:
        return builder(item, manager)
    