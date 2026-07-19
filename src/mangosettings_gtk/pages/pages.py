import gi
from gi.repository import Adw
from . import general, sound, wallpaper, about

builders = {
    "general": general.build,
    #"apps": apps.build,
    #"bluetooth": bluetooth.build,
    "sound": sound.build,
    #"power": power.build,
    #"display": display.build,
    #"keyboard": keyboard.build,
    #"shortcuts": shortcuts.build,
    #"mouse": mouse.build,
    #"appearance": appearance.build,
    #"animations": animations.build,
    "wallpaper": wallpaper.build,
    "about": about.build

}


def build_page(page_id):
    if page_id not in builders:
        return Adw.StatusPage(title=page_id, description="Yapım aşamasında")
    builder = builders[page_id]
    return builder()