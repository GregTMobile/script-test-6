import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sh

class RebuildHandler(FileSystemEventHandler):
    def on_any_event(self, event):
       if event.src_path.endswith('json') or event.src_path.endswith('md'):
          sh('./build-all.sh')

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = RebuildHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
