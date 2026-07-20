import gi
gi.require_version("Gtk","4.0")
from gi.repository import Gtk, GLib
from .window import MangoWindow
from .config.manager import ConfigManager

class MangoSettings(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.mango.settings") #id değişecek
    
    def do_activate(self):
        config = ConfigManager()
        extra_files = config.find_extra_files()
        window = MangoWindow(application=self)
        window.present()
        
        if extra_files:
            GLib.idle_add(self.warning_about_split_config, window, extra_files)
    
    def warning_about_split_config(self, window, extra):
        alert = Gtk.AlertDialog()
        alert.set_modal(True)
        alert.set_message("Birden fazla config dosyası bulundu")
        files = "\n".join(str(x) for x in extra)
        alert.set_detail("config.conf disinda su dosyalar var:\n\n"
            f"{files}\n\n"
            "Bu uygulama sadece config.conf dosyasini okur ve yazar. "
            "Ayarlarını `source=` ile birden fazla dosyaya böldüysen, "
            "bu aracı kullanmadan önce hepsini tek bir config.conf "
            "dosyasında birleştirmen onerilir; aksi halde diğer "
            "dosyalardaki ayarlar bu arayüzde görünmez ve değiştirilemez."
        )
        alert.set_buttons(["Anladım"])
        alert.show(window)
        return False
