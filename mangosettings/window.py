import gi
gi.require_version("Gtk","4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from .ui.sidebar import Sidebar
from .pages.pages import build_page
from .config.manager import ConfigManager


class MangoWindow(Adw.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config = ConfigManager()

        self.set_title("Mango Settings")
        self.set_default_size(1600,900)
        #self.set_size_request() #en düşük galiba

        self.page_cache = {}
         
        self.split = Adw.NavigationSplitView(min_sidebar_width=200, max_sidebar_width=300)
        self.set_content(self.split)


        self.sidebar = Sidebar(on_page_selected=self.show_page)
        self.split.set_sidebar(self.sidebar.sidebar_page)
        #self.build_sidebar()
        self.build_content()
        #self.build_breakpoint() #denicem

        self.show_page("general")



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