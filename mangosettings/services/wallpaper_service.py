import subprocess
import os

valid = (".gif", ".png", ".jpg", ".jpeg", ".webp")

class WallpaperService():
    def __init__(self):
        self.wallpaper_path = None
        self.check_daemon()

    def check_daemon(self):
        try:
            subprocess.run(["awww", "query"])
        except FileExistsError:
            subprocess.Popen(["awww-daemon"])

    def set_path(self,path):
        self.wallpaper_path = path
    
    def get_wallpapers(self):
        if not self.wallpaper_path:
            return []
        wallpapers = []
        for filename in sorted(os.listdir(self.wallpaper_path)):
            full_path = os.path.join(self.wallpaper_path, filename)
            if os.path.isfile(full_path) and filename.lower().endswith(valid):
                wallpapers.append(full_path)
 
        return wallpapers

    
    def change_wallpaper(self, wallpaper):
        subprocess.run(["awww", "img", wallpaper])
