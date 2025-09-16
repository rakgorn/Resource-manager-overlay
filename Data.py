import psutil
import GPUtil
from screeninfo import get_monitors  


class ComData():
    def cpu(self):
        return f"CPU %:{psutil.cpu_percent(interval=None)}"
    def ram(self):
        return f"RAM %:{psutil.virtual_memory().percent}"
    def gpu_temp(self):
        gpu = GPUtil.getGPUs()[0]
        return f"GPU TEMP:{gpu.temperature}°C"
    def monitor(self):
        monitor=get_monitors()[0]
        return [monitor.width,monitor.height]
   