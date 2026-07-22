import gi
from gi.repository import Adw
from . import general, sound, power, wallpaper, about
from .generic import build_generic
from ..schemas.schema import get_schema_page

builders = {
    "general": general.build,
    #"apps": apps.build,
    #"bluetooth": bluetooth.build,
    "sound": sound.build,
    "power": power.build,
    #"display": display.build,
    #"keyboard": keyboard.build,
    #"shortcuts": shortcuts.build,
    #"mouse": mouse.build,
    #"appearance": appearance.build,
    #"animations": animations.build,
    "wallpaper": wallpaper.build,
    #"layout": layout.build,
    #"overview": overview.build,
    #"window-rules": window-rules.build,
    #"layer-rules": layer-rules.build,
    #"tag-rules": tag-rules.build,
    #"misc": misc.build,
    "about": about.build

}


def build_page(page_id, manager):
    if page_id in builders:
        return builders[page_id](manager)

    schema = get_schema_page(page_id)
    if schema:
        return build_generic(schema, manager)

    return Adw.StatusPage(title=page_id,description="Yapım aşamasında")