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

    def get_gpu(self):
        gpus = []
        for path in glob.glob("/sys/class/drm/card*/device/vendor"):
            with open(path) as f:
                vendor = f.read().strip()
            gpus.append(vendor)
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