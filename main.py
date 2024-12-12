import asyncio
from Scripts.downloader import download_video
from Scripts.monitor import monitor_videos,detect_new_file
from networkx import is_path 


async def main():
    instagram_url = "https://www.instagram.com/reel/DDW7W1jMjWT/?igsh=MTViMTA5Y3ljZ2Zicg=="

    print("Starting video downloads and monitoring...")
    await asyncio.gather(
        download_video(instagram_url),
        monitor_videos()
    )

if __name__ == "__main__":
   import time

def monitor_directory(directory):
    print(f"Monitoring directory: {directory}")
    monitoring = True
    while monitoring:
        try:
            print("Still monitoring...")
            # Simulate detecting files
            file_path = detect_new_file(directory)
            if file_path:
                print(f"Handling file: {file_path}")
                # Process file logic here
                monitoring = False  # Exit condition for demonstration
            else:
                print("No new files detected.")
            time.sleep(5)
        except Exception as e:
            print(f"Error during monitoring: {e}")
            monitoring = False
    print("Monitoring stopped.")

if __name__ == "__main__":
    asyncio.run(main())
