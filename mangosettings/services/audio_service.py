import subprocess
import re

class AudioService():
    def __init__(self):
        self.sinks = []
        self.get_sinks()
    
    def get_sinks(self):
        self.sinks.clear()
        inside_sinks = False
        output = subprocess.run(["wpctl", "status"],capture_output=True,text=True)
        for line in output.stdout.splitlines():
            if "Sinks:" in line:
                inside_sinks = True
                continue
            if inside_sinks:
                if "Sources:" in line:
                    inside_sinks = False
                    break  
                match = re.search(r"(\d+)\.\s+(.*?)\s+\[", line)
                if match:
                    self.sinks.append({
                        "id": int(match.group(1)),
                        "name": match.group(2),
                        "default": "*" in line })
        return self.sinks

    def set_default_sink(self, sink_id):
        subprocess.run(["wpctl", "set-default", str(sink_id)])

    def get_volume(self):
        output = subprocess.run(["wpctl","get-volume","@DEFAULT_AUDIO_SINK@"],capture_output=True,text=True)
        match = re.search(r"(\d+\.\d+)",output.stdout)
        if match:
            return float(match.group(1)) * 100

        return 0

    def set_volume(self, value):
        subprocess.run(["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", str(value / 100)])
    
    def get_mute(self):
        output = subprocess.run(["wpctl", "get-volume", "@DEFAULT_AUDIO_SINK@"],capture_output=True, text=True)
        return "MUTED" in output.stdout

    def set_mute(self,state):
        subprocess.run(["wpctl", "set-mute", "@DEFAULT_AUDIO_SINK@", "1" if state else "0"])

