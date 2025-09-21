#!/usr/bin/env python3
"""
Application Health Checker Script
Monitors HTTP status of web applications
Reports UP/DOWN status with response times
"""

import requests
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app_health.log'),
        logging.StreamHandler()
    ]
)

# Configuration
APPS = [
    {
        'name': 'Wise Cow Application',
        'url': 'http://localhost:4499',
        'expected_status': 200,
        'timeout': 10
    },
    # Add more apps here if needed
    # {
    #     'name': 'Another Service',
    #     'url': 'http://example.com',
    #     'expected_status': 200,
    #     'timeout': 5
    # }
]

CHECK_INTERVAL = 30  # seconds between checks

def check_app_health(app_config):
    """Check health of a single application"""
    app_name = app_config['name']
    url = app_config['url']
    expected_status = app_config['expected_status']
    timeout = app_config['timeout']
    
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        response_time = time.time() - start_time
        
        status_code = response.status_code
        if status_code == expected_status:
            message = f" {app_name}: UP | Status: {status_code} | Response: {response_time:.2f}s"
            logging.info(message)
            print(message)
            return {'status': 'UP', 'response_time': response_time}
        else:
            message = f" {app_name}: DOWN | Status: {status_code} (expected {expected_status}) | Response: {response_time:.2f}s"
            logging.error(message)
            print(message)
            return {'status': 'DOWN', 'status_code': status_code, 'response_time': response_time}
            
    except requests.exceptions.Timeout:
        message = f" {app_name}: TIMEOUT | URL: {url} | Timeout: {timeout}s"
        logging.error(message)
        print(message)
        return {'status': 'TIMEOUT', 'response_time': timeout}
    except requests.exceptions.ConnectionError:
        message = f" {app_name}: CONNECTION ERROR | URL: {url} unreachable"
        logging.error(message)
        print(message)
        return {'status': 'CONNECTION_ERROR'}
    except Exception as e:
        message = f" {app_name}: UNKNOWN ERROR | {str(e)}"
        logging.error(message)
        print(message)
        return {'status': 'ERROR', 'error': str(e)}

def health_report():
    """Generate complete application health report"""
    print(f"\n{'='*60}")
    print(f"Application Health Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    
    results = {}
    for app in APPS:
        result = check_app_health(app)
        results[app['name']] = result
    
    # Summary
    print(f"\n Health Summary:")
    up_count = sum(1 for r in results.values() if r['status'] == 'UP')
    total_count = len(results)
    print(f"   UP: {up_count}/{total_count} applications")
    
    for app_name, result in results.items():
        status = result['status']
        if status == 'UP':
            print(f"    {app_name}: {status}")
        else:
            print(f"    {app_name}: {status}")
    
    print(f"{'='*60}\n")
    return results

def main():
    """Main monitoring loop"""
    print(" Application Health Monitor Started...")
    print(f" Checking every {CHECK_INTERVAL} seconds | Logs: app_health.log")
    print(f" Monitoring: {', '.join([app['name'] for app in APPS])}\n")
    
    try:
        while True:
            health_report()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print(f"\n Application Health Monitor Stopped by User")
        logging.info("Application Health Monitor stopped")

if __name__ == "__main__":
    main()
