import psutil
import time
from datetime import datetime

# print(psutil)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    total = mem.total / (1024 ** 3)
    used = mem.used / (1024 ** 3)
    free = mem.free / (1024 ** 3)
    return {'total': total, 'used': used, 'free': free, 'percent': mem.percent}

def get_disk_io():
    disk_io = psutil.disk_io_counters()
    return {
        'read_bytes': disk_io.read_bytes / (1024 ** 2),
        'write_bytes': disk_io.write_bytes / (1024 ** 2)
    }

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    total = disk_usage.total / (1024 ** 3)
    used = disk_usage.used / (1024 ** 3)
    free = disk_usage.free / (1024 ** 3)
    return {'total': total, 'used': used, 'free': free, 'percent': disk_usage.percent}

def get_network_io():
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent / (1024 ** 2),
        'bytes_recv': net_io.bytes_recv / (1024 ** 2)
    }

def display_stats():
    print("="*40)
    print(f"Server Performance Stats at {datetime.now()}")
    print("="*40)
    
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage: {cpu_usage}%")
    
    memory_usage = get_memory_usage()
    print(f"Memory Usage: {memory_usage['used']:.2f} GB / {memory_usage['total']:.2f} GB ({memory_usage['percent']}%)")
    
    disk_usage = get_disk_usage()
    print(f"Disk Usage: {disk_usage['used']:.2f} GB / {disk_usage['total']:.2f} GB ({disk_usage['percent']}%)")
    
    disk_io = get_disk_io()
    print(f"Disk I/O - Read: {disk_io['read_bytes']:.2f} MB, Write: {disk_io['write_bytes']:.2f} MB")
    
    network_io = get_network_io()
    print(f"Network I/O - Sent: {network_io['bytes_sent']:.2f} MB, Received: {network_io['bytes_recv']:.2f} MB")
    print("="*40)

if __name__ == "__main__":
    try:
        while True:
            display_stats()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
