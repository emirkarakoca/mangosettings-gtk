import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

from ..ui.rows import create_row

def build_generic(page_data,manager):
    page = Adw.PreferencesPage()
    for group_data in page_data:
        group = Adw.PreferencesGroup(title=group_data["title"])
        for item in group_data["items"]:
            row = create_row(item, manager)
            if row:
                group.add(row)
        page.add(group)
    return page