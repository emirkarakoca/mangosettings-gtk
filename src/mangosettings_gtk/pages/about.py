import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from ..services.info_service import InfoService
import time
def build():
    info = InfoService()
    
    start = time.time()
    mem_info = info.get_memory()
    print("MEM:", time.time() - start)
    start = time.time()    
    disk_info = info.get_disk()
    print("DISK:", time.time() - start)
    start = time.time()
    gpu_info = info.get_gpu() #sorunlu
    print("GPU:", time.time() - start)
    page = Adw.PreferencesPage(title="Hakkında") #,,

    device = Adw.PreferencesGroup(title="Cihaz")
    manufacturer = Adw.ActionRow(title="Üretici",subtitle=info.get_manufacturer())
    device.add(manufacturer)
    model = Adw.ActionRow(title="Cihaz Modeli",subtitle=info.get_model())
    device.add(model)
    hostname = Adw.ActionRow(title="Cihaz Adı",subtitle=info.get_hostname())
    device.add(hostname)
    page.add(device)
    
    hardware = Adw.PreferencesGroup(title="Donanım")
    cpu = Adw.ActionRow(title="İşlemci",subtitle=info.get_cpu())
    hardware.add(cpu)
    gpu = Adw.ActionRow(title="GPU",subtitle="\n".join(gpu_info) if gpu_info else "Bilinmeyen")
    hardware.add(gpu)
    memory = Adw.ActionRow(title="Bellek",subtitle=f"{mem_info["used"]}/{mem_info["total"]}")
    hardware.add(memory)
    page.add(hardware)
    
    os_group = Adw.PreferencesGroup(title="İşletim Sistemi")
    distro = Adw.ActionRow(title="Dağıtım",subtitle=info.get_distro())
    os_group.add(distro)
    kernel = Adw.ActionRow(title="Çekirdek",subtitle=info.get_kernel())
    os_group.add(kernel)
    desktop = Adw.ActionRow(title="Masaüstü",subtitle=info.get_desktop())
    os_group.add(desktop)
    session = Adw.ActionRow(title="Oturum",subtitle=info.get_session())
    os_group.add(session)
    page.add(os_group)
    
    #software = Adw.PreferencesGroup(title="Yazılım") belki
    #page.add(software)
    
    power = Adw.PreferencesGroup(title="Pil")
    state = Adw.ActionRow(title="Durum",subtitle=info.get_battery_state())
    power.add(state)
    battery = Adw.ActionRow(title="Kalan",subtitle=info.get_battery_percent())
    power.add(battery)
    battery_health = Adw.ActionRow(title="Sağlık",subtitle=info.get_battery_health())
    power.add(battery_health)
    page.add(power)
    
    storage = Adw.PreferencesGroup(title="Depolama")
    disk_used = Adw.ActionRow(title="Kullanılan",subtitle=disk_info["used"])
    storage.add(disk_used)
    disk_total = Adw.ActionRow(title="Toplam",subtitle=disk_info["total"])
    storage.add(disk_total)
    disk_usage = Adw.ActionRow(title="Kullanım", subtitle=disk_info["usage"])
    storage.add(disk_usage)
    page.add(storage)
    
    return page