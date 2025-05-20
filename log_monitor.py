import time
import os
from parser import is_alert
from alert import send_console_alert
import logging

LOG_PATH = "logs/sample_app.log"

logging.basicConfig(filename='monitor.log', level=logging.INFO)

def tail_log(file_path):
    with open(file_path, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            logging.info(f"Read line: {line.strip()}")
            if is_alert(line):
                send_console_alert(line.strip())

if __name__ == "__main__":
    print("Monitoring started...")
    tail_log(LOG_PATH)
