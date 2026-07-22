import gi
gi.require_version("Gtk","4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from .. import registry

class Sidebar:
    def __init__(self, on_page_selected=None):
        self.sidebar_items = []
        self.on_page_selected = on_page_selected
        self.build_sidebar()
    
    def build_sidebar(self):
        self.sidebar = Adw.Sidebar()
        self.sidebar.connect("activated", self.on_sidebar_activated)
        
        
        for section_title, items in registry.get_categories():
            section = Adw.SidebarSection(title=section_title)
            for page_id, title, icon in items:
                item = Adw.SidebarItem(title=title, icon_name=icon)
                item.page_id = page_id
                self.sidebar_items.append(item)
                section.append(item)
            self.sidebar.append(section)
        
        toolbarview = Adw.ToolbarView()
        header = Adw.HeaderBar()
        header.set_title_widget(Adw.WindowTitle(title="Mango Ayarları"))  
        
        self.search_button = Gtk.ToggleButton(icon_name="system-search-symbolic")
        self.search_button.connect("toggled", self.on_toggle_search)
        header.pack_start(self.search_button)

        self.revealer = Gtk.Revealer()
        self.revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_DOWN)
        
        self.search_entry = Gtk.SearchEntry()
        
        self.search_entry.connect("search-changed", self.on_search_changed)
        self.search_entry.connect("activate", self.on_search_activate)
        self.search_entry.connect("stop-search", self.on_stop_search)
        
        self.revealer.set_child(self.search_entry)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.append(self.revealer)
        box.append(self.sidebar)

        toolbarview.add_top_bar(header)
        toolbarview.set_content(box)       
        
        self.sidebar_page = Adw.NavigationPage(child=toolbarview)

    def on_sidebar_activated(self, sidebar, index):
        selected_item = sidebar.get_item(index)
        if self.on_page_selected:
            self.on_page_selected(selected_item.page_id)

    def on_toggle_search(self, button):
        active = button.get_active()
        self.revealer.set_reveal_child(active)
        if active:
            self.search_entry.grab_focus()
        else:
            self.search_entry.set_text("")
            
    def on_search_changed(self, entry):
        text = entry.get_text().lower().strip()
        for item in self.sidebar_items:
            title = item.get_title().lower()
            item.set_visible(text in title)
    
    def on_search_activate(self, entry):
        for index, item in enumerate(self.sidebar_items):
            if item.get_visible():
                self.sidebar.set_selected(index)
                if self.on_page_selected:
                    self.on_page_selected(item.page_id)
                break
    
    def on_stop_search(self, entry):
        self.search_entry.set_text("")
        self.revealer.set_reveal_child(False)
        self.search_button.set_active(False)
        return True        