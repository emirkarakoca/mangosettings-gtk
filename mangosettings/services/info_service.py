import platform
import subprocess
import os
import glob

class InfoService():
    def __init__(self):
        pass

    def get_manufacturer(self):
        try:
            with open("/sys/class/dmi/id/sys_vendor") as f:
                return f.read().strip()
        except:
            return "Bilinmeyen"

    def get_model(self):
        try:
            with open("/sys/class/dmi/id/product_name") as f:
                return f.read().strip()
        except:
            return "Bilinmeyen"

    def get_hostname(self):
        try:
            with open("/etc/hostname") as f:
                return f.read().strip()
        except:
            return "Bilinmeyen"

    def get_cpu(self):
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("model name"):
                    return line.split(":")[1].strip()
            return "Bilinmeyen"

    def _load_pci_ids(self): #nasıl çalıştığını dahi bilmiyorum claude baba yaptı
        paths = ["/usr/share/misc/pci.ids", "/usr/share/hwdata/pci.ids", "/usr/share/pci.ids"]
        pci_ids_path = next((p for p in paths if os.path.exists(p)), None)
        if not pci_ids_path:
            return {}
        vendors = {}
        current_vendor = None
        try:
            with open(pci_ids_path, encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if line.startswith("#") or not line.strip():
                        continue
                    if line.startswith("\t\t"):
                        continue
                    if line.startswith("\t"):
                        if current_vendor is None:
                            continue
                        parts = line.strip().split(None, 1)
                        if len(parts) == 2:
                            dev_id, dev_name = parts
                            vendors[current_vendor][1][dev_id.lower()] = dev_name.strip()
                        continue
                    if line[0] == "C":
                        break
                    parts = line.strip().split(None, 1)
                    if len(parts) == 2:
                        vendor_id, vendor_name = parts
                        current_vendor = vendor_id.lower()
                        vendors[current_vendor] = (vendor_name.strip(), {})
        except Exception:
            return {}
        return vendors

    def get_gpu(self): #aynı şekilde
        pci_ids = self._load_pci_ids()
        gpus = []
        for dev_path in glob.glob("/sys/bus/pci/devices/*/"):
            class_file = os.path.join(dev_path, "class")
            if not os.path.exists(class_file):
                continue
            with open(class_file) as f:
                pci_class = f.read().strip()
            if pci_class in ("0x030000", "0x030200", "0x038000"):
                with open(os.path.join(dev_path, "vendor")) as f:
                    vendor_id = f.read().strip().replace("0x", "").lower()
                with open(os.path.join(dev_path, "device")) as f:
                    device_id = f.read().strip().replace("0x", "").lower()

                vendor_name = "Bilinmeyen"
                device_name = "Bilinmeyen"
                if vendor_id in pci_ids:
                    vendor_name, devices = pci_ids[vendor_id]
                    device_name = devices.get(device_id, "Bilinmeyen")
                gpus.append({
                    "vendor_id": vendor_id,
                    "device_id": device_id,
                    "vendor": vendor_name,
                    "device": device_name,
                    "name": f"{vendor_name} {device_name}"
                })
        return gpus

    def get_memory(self):
        values = {}
        try:
            with open("/proc/meminfo") as f:
                for line in f:
                    key, value = line.split(":")
                    values[key] = int(value.split()[0])
                total = values["MemTotal"]
                available = values["MemAvailable"]
                used = total - available
                
                return {"total": f"{total/1048576:.1f} GB", "used": f"{used/1048576:.1f} GB"}
        except:
            return "Bilinmeyen"

    def get_distro(self):
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME"):
                        return line.split("=")[1].replace('"', "").strip()
        except:
            return "Bilinmeyen"

    def get_kernel(self):
        try:
            return platform.release()
        except:
            return "Bilinmeyen"

    def get_desktop(self):
        try:
            return os.environ.get("XDG_CURRENT_DESKTOP", "Bilinmeyen")
        except:
            return "Bilinmeyen"

    def get_session(self):
        try:
            return os.environ.get("XDG_SESSION_TYPE", "Bilinmeyen")
        except:
            return "Bilinmeyen"
    
    def get_battery_state(self):
        try:
            with open("/sys/class/power_supply/BAT0/status") as f:
                status = f.read().strip()
            with open("/sys/class/power_supply/BAT0/capacity") as f:
                capacity = int(f.read().strip())
            if status == "Not charging" and capacity >= 99:
                return "Dolu"
            
            states = {
                "Charging": "Şarj Oluyor", "Discharging": "Bataryada",
                "Full": "Dolu", "Not charging": "Şarj Olmuyor"}
            return states.get(status,status)
        except:
            return "Bilinmeyen"
    
    def get_battery_percent(self):
        try:
            with open("/sys/class/power_supply/BAT0/capacity") as f:
                return f"%{f.read().strip()}"
        except:
            return "Bilinmeyen"

    def get_battery_health(self):
        try:
            for name in ["energy_full", "charge_full"]:
                try:
                    with open(f"/sys/class/power_supply/BAT0/{name}") as f:
                        full = int(f.read())
                        break
                except:
                    pass
            for name in ["energy_full_design", "charge_full_design"]:
                try:
                    with open(f"/sys/class/power_supply/BAT0/{name}") as f:
                        design = int(f.read())
                        break
                except:
                    pass
            health = (full / design) * 100
            return f"%{health:.0f}"

        except:
            return "Bilinmeyen"

    def get_disk(self):
        try:
            result = subprocess.run(["df", "-BG", "/"],capture_output=True,text=True)
            values = result.stdout.splitlines()[1].split()
            return {
                "total": values[1],
                "used": values[2],
                "free": values[3],
                "usage": values[4] }

        except Exception as e:
            print(e)
            return "Bilinmeyen"