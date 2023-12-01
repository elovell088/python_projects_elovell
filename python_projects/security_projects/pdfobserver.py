import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.pdf'):  # Replace '.pdf' with your PDF filename or pattern
            # Open Excel when PDF is modified
            subprocess.Popen(['excel'])  # Adjust this command as needed for your system

if __name__ == "__main__":
    path = "/path/to/directory"  # Replace this with the directory path where your PDF is located
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
