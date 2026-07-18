import gi
gi.require_version("Gtk","4.0")
from gi.repository import Gtk
from .window import MangoWindow

class MangoSettings(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.mango.settings") #id değişecek
    
    def do_activate(self):
        window = MangoWindow(application=self)
        window.present()