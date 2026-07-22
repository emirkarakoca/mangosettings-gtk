import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib
from ..services.wallpaper_service import WallpaperService

def build(_):
    ws = WallpaperService()
    page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    content = Adw.PreferencesPage(vexpand=True)
    wall_group = Adw.PreferencesGroup(title="Duvar Kağıtları")
    
    wall_box = Adw.WrapBox(child_spacing=10,line_spacing=10)
    wall_box.set_hexpand(True)
    wall_box.set_vexpand(True)
    wall_group.add(wall_box)
    content.add(wall_group)
    page.append(content)

    state = {"path": None, "leader": None}

    def on_toggle(w, path):
        if w.get_active():
            state["path"] = path
            apply_button.set_sensitive(True)

    def clearw():
        child = wall_box.get_first_child()
        while child is not None:
            next_child = child.get_next_sibling()
            wall_box.remove(child)
            child = next_child
        state["leader"] = None
        state["path"] = None

    def show_wallpapers():
        clearw()
        apply_button.set_sensitive(False)
        wallpapers = ws.get_wallpapers()
        for path in wallpapers:
            image = Gtk.Image(file=path,pixel_size=200)
            toggle = Gtk.ToggleButton()
            toggle.set_child(image)
            if state["leader"] is None:
                state["leader"] = toggle
            else:
                toggle.set_group(state["leader"])
            
            toggle.connect("toggled", on_toggle, path)
            wall_box.append(toggle)

    def on_folder_chosen(dialog, result):
        try:
            folder = dialog.select_folder_finish(result)
        except GLib.Error:
            return
        if folder is not None:
            ws.set_path(folder.get_path())
            show_wallpapers()

    def on_choose_f_clicked(_):
        dialog = Gtk.FileDialog()
        dialog.select_folder(None, None, on_folder_chosen)

    def on_apply_clicked(_):
        if state["path"]:
            ws.change_wallpaper(state["path"])

    bar = Gtk.ActionBar()  
    choose_f_button = Gtk.Button(label="Klasör Seç")     
    choose_f_button.connect("clicked", on_choose_f_clicked)
    bar.pack_start(choose_f_button)

    apply_button = Gtk.Button(label="Onayla")
    apply_button.set_sensitive(False)
    apply_button.connect("clicked", on_apply_clicked)
    bar.pack_end(apply_button)

    page.append(bar)
    if ws.wallpaper_path:
        show_wallpapers()

    return page