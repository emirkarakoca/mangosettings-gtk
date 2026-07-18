import gi
from gi.repository import Adw
from . import general, sound, about

builders = {
    "general": general.build,
    "sound": sound.build,
    "about": about.build
}


def build_page(page_id):
    if page_id not in builders:
        return Adw.StatusPage(title=page_id, description="Yapım aşamasında")
    builder = builders[page_id]
    return builder()