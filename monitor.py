import time
import os
import threading
from custom_uploader import get_upload_url, upload_video, upload
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def create_post(title, video_hash):
    print(f"Post created with title: {title} and hash: {video_hash}")

class VideoHandler(FileSystemEventHandler):
        def on_created(self, event):
           if event.src_path.endswith(".mp4"):
            print(f"New MP4 file detected: {event.src_path}")
            threading.Thread(target=self.handle_mp4, args=(event.src_path,)).start()
           else:
            print(f"Ignored non-MP4 file: {event.src_path}")

        def handle_mp4(self, filepath):
           try:
            print(f"Handling file: {filepath}")
            upload_url, video_hash = get_upload_url()
            print("Upload URL obtained, starting upload...")
            upload_video(filepath, upload_url)
            print("Upload completed, creating post...")
            os.remove(filepath)
            print(f"Upload complete and file deleted: {filepath}")
           except Exception as e:
            print(f"Error during upload: {e}")
            
def monitor_videos(directory="videos"):
    import os
    import time
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    class VideoHandler(FileSystemEventHandler):
        def on_created(self, event):
            if event.src_path.endswith(".mp4"):
                print(f"New MP4 file detected: {event.src_path}")
            else:
                print(f"Ignored non-MP4 file: {event.src_path}")

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

    print(f"Monitoring directory: {directory}")
    event_handler = VideoHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()

    try:
        while True:
            print("Still monitoring...")
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoring stopped.")
    observer.join()

def detect_new_file(directory):
    files = os.listdir(directory)
    print(f"Checking for new files in {directory}...")
    print(f"Files in {directory}: {files}")
    return os.path.join(directory, files[0]) if files else None

def monitor_directory(directory="videos"):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

    print(f"Monitoring directory: {directory}")
    try:
        while True:
            print("Still monitoring...")
            file_path = detect_new_file(directory)
            if file_path:
                print(f"Handling file: {file_path}")
                try:
                    result = upload(file_path)
                    if result is None:
                        raise ValueError("Upload returned None")
                    status, file_id = result
                    print(f"File uploaded successfully: {status}, {file_id}")
                    os.remove(file_path)
                    print(f"File deleted: {file_path}")
                except Exception as e:
                    print(f"Error during file handling: {e}")
            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_directory()
