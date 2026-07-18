import gi
gi.require_version("Gtk","4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from . import categories
from .pages.pages import build_page

class MangoWindow(Adw.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title("Mango Settings")
        self.set_default_size(900,750)
        #self.set_size_request() #en düşük galiba

        self.page_cache = {}
         
        self.split = Adw.NavigationSplitView(min_sidebar_width=200, max_sidebar_width=300)
        self.set_content(self.split)

        self.build_sidebar()
        self.build_content()
        #self.build_breakpoint() #denicem

        self.show_page("general")

    def build_sidebar(self):
        self.sidebar = Adw.Sidebar()
        self.sidebar.connect("activated", self.on_sidebar_activated)
        for section_title, items in categories.category_list:
            section = Adw.SidebarSection(title=section_title)
            for page_id, title, icon in items:
                item = Adw.SidebarItem(title=title, icon_name=icon)
                item.page_id = page_id
                section.append(item)
            self.sidebar.append(section)

        #search buraya
        
        toolbarview = Adw.ToolbarView()
        header = Adw.HeaderBar()
        header.set_title_widget(Adw.WindowTitle(title="Mango Ayarları"))  
        toolbarview.add_top_bar(header)
        toolbarview.set_content(self.sidebar)       
        
        self.sidebar_page = Adw.NavigationPage(title="Mango Ayarları", child=toolbarview)
        self.split.set_sidebar(self.sidebar_page)

    def build_content(self):
        self.stack = Adw.ViewStack()
        
        toolbarview = Adw.ToolbarView()
        self.contentheader = Adw.HeaderBar()
        self.contentheader.set_title_widget(Gtk.Label())
        toolbarview.add_top_bar(self.contentheader)
        toolbarview.set_content(self.stack)

        self.content_page = Adw.NavigationPage(title="İçerik", child=toolbarview)
        self.split.set_content(self.content_page)

    def on_sidebar_activated(self, sidebar, index):
        selected_item = sidebar.get_item(index)
        self.show_page(selected_item.page_id)
    
    def show_page(self, page_id):
        if page_id not in self.page_cache:
            page = build_page(page_id)
            self.page_cache[page_id] = page
            print(self.page_cache)
            self.stack.add_named(page,page_id)
        self.stack.set_visible_child_name(page_id)