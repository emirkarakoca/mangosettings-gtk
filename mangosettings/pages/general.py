import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

def build(manager):
    page = Adw.StatusPage(title="Hoş Geldiniz",description="Şimdilik Boş",icon_name="face-cool-symbolic")
    return page