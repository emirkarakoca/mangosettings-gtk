import subprocess
class MangoService:
    def reload_config(self):
        subprocess.run(["mmsg","dispatch","reload_config"],check=False)