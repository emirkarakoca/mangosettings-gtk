import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from ..config.manager import ConfigManager
from ..schemas.mango import PAGES
from ..ui.rows import create_row

manager = ConfigManager()

def build():
    page = Adw.PreferencesPage()
    page_data = next(p for p in PAGES if p["page"] == "mouse")
    for group_data in page_data["groups"]:
        group = Adw.PreferencesGroup(title=group_data["title"])
        for item in group_data["items"]:
            row = create_row(item, manager)
            if row:
                group.add(row)
        page.add(group)

    return page