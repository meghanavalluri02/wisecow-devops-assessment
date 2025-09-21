#!/usr/bin/env python3
"""
System Health Monitoring Script
Monitors CPU, memory, disk usage and running processes
Alerts if thresholds exceeded
"""

import psutil
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('system_health.log'),
        logging.StreamHandler()
    ]
)

# Thresholds (customizable)
THRESHOLDS = {
    'cpu': 80,      # CPU % threshold
    'memory': 80,   # Memory % threshold
    'disk': 85,     # Disk % threshold
    'processes': 500 # Max processes
}

def check_cpu():
    """Check CPU usage"""
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > THRESHOLDS['cpu']:
        message = f"ALERT: CPU usage high - {cpu_percent}% (> {THRESHOLDS['cpu']}%)"
        logging.warning(message)
        print(message)
    else:
        logging.info(f"CPU: {cpu_percent:.1f}% (OK)")
    return cpu_percent

def check_memory():
    """Check memory usage"""
    memory = psutil.virtual_memory()
    mem_percent = memory.percent
    if mem_percent > THRESHOLDS['memory']:
        message = f"ALERT: Memory usage high - {mem_percent}% (> {THRESHOLDS['memory']}%)"
        logging.warning(message)
        print(message)
    else:
        logging.info(f"Memory: {mem_percent:.1f}% ({memory.available // (1024**3)}GB free)")
    return mem_percent

def check_disk():
    """Check disk usage"""
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    if disk_percent > THRESHOLDS['disk']:
        message = f"ALERT: Disk usage high - {disk_percent}% (> {THRESHOLDS['disk']}%)"
        logging.warning(message)
        print(message)
    else:
        logging.info(f"Disk: {disk_percent:.1f}% ({disk.free // (1024**3)}GB free)")
    return disk_percent

def check_processes():
    """Check number of running processes"""
    process_count = len(psutil.pids())
    if process_count > THRESHOLDS['processes']:
        message = f"ALERT: Process count high - {process_count} (> {THRESHOLDS['processes']})"
        logging.warning(message)
        print(message)
    else:
        logging.info(f"Processes: {process_count}")
    return process_count

def system_health_report():
    """Generate complete system health report"""
    print(f"\n{'='*50}")
    print(f"System Health Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")
    
    cpu = check_cpu()
    mem = check_memory()
    disk = check_disk()
    procs = check_processes()
    
    print(f"\n📊 Summary:")
    print(f"   CPU: {cpu:.1f}%")
    print(f"   Memory: {mem:.1f}%")
    print(f"   Disk: {disk:.1f}%")
    print(f"   Processes: {procs}")
    print(f"{'='*50}\n")

def main():
    """Main monitoring loop"""
    print("  System Health Monitor Started...")
    print(f" Checking every 60 seconds | Logs: system_health.log")
    print(f"⚠️  Thresholds: CPU={THRESHOLDS['cpu']}%, Mem={THRESHOLDS['memory']}%, Disk={THRESHOLDS['disk']}%\n")
    
    try:
        while True:
            system_health_report()
            time.sleep(60)  # Wait 60 seconds
    except KeyboardInterrupt:
        print("\n System Health Monitor Stopped by User")
        logging.info("System Health Monitor stopped")

if __name__ == "__main__":
    main()
