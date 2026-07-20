from pathlib import Path
import shutil

MULTI_KEYS = {"exec-once", "exec", "bind", "mousebind", "axisbind",
    "layerrule", "tagrule", "monitorrule", "env", 
    "source", "source-optional"}

class ConfigManager():
    def __init__(self):
        self.conf = Path.home() / ".config" / "mango" / "config.conf"
        self.default = Path(__file__).parent.parent.parent / "data" / "config.conf"
        self.settings = {}
        self.value_line_index = {}
        self.lines = []
        
        if not self.conf.exists():
            self.create_config()
        self.load()

    def create_config(self):
        self.conf.parent.mkdir(parents=True,exist_ok=True)
        if not self.conf.exists():
            shutil.copy(self.default, self.conf)

    def load(self):
        with self.conf.open("r", encoding="utf-8") as file:
            self.lines = file.read().splitlines()
            for index, line in enumerate(self.lines):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                if key in MULTI_KEYS:
                    continue
                value = value.strip()
                if "#" in value:
                    value = value.split("#", 1)[0].strip()
                self.settings[key] = value
                self.value_line_index[key] = index
    
    def get(self, key):
        return self.settings.get(key)

    def get_bool(self, key, default):
        b = self.settings.get(key)
        if b is None:
            return default
        return b.strip().lower() in ("1", "true", "yes")

    def get_int(self, key, default):
        try:
            return int(self.settings.get(key, default))
        except (TypeError, ValueError):
            return default

    def get_float(self, key, default):
        try:
            return float(self.settings.get(key, default))
        except (TypeError,ValueError):
            return default
        
    def set(self, key, value):
        if isinstance(value, bool):
            value = "1" if value else "0"
        elif isinstance(value, float):
            value = f"{value:.6f}".rstrip("0").rstrip(".")
        else:
            value = str(value)
            
        self.settings[key] = value
        if key in self.value_line_index:
            index = self.value_line_index[key]
            old = self.lines[index]
            indentation = old[:(len(old)-len(old.lstrip()))]
            comment = ""
            if "#" in old:
                after_equal = old.split("=", 1)[1] if "=" in old else ""
                if "#" in after_equal:
                    comment = " #" + after_equal.split("#", 1)[1]
            self.lines[index] = f"{indentation}{key}={value}{comment}"
        else:
            self.lines.append(f"{key}={value}") #tekrarlanabilirler için
            self.value_line_index[key] = len(self.lines) - 1
        self.save()

    def save(self):
        backup = self.conf.with_suffix(self.conf.suffix + ".bak")
        backup.write_text(self.conf.read_text(encoding="utf-8"), encoding="utf-8")
        self.conf.write_text("\n".join(self.lines),encoding="utf-8")

    def find_extra_files(self):
        main_resolved = self.conf.resolve()
        extras = []
        for candidate in self.conf.parent.rglob("*.conf"):
            if candidate.is_dir():
                continue
            if candidate.resolve() == main_resolved:
                continue
            extras.append(candidate)
        
        return extras