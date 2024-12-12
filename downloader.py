import os
import re

def download_video(instagram_url):
    # Generate a filename based on the URL (this is just an example)
    filename = f"videos\\{instagram_url.split('?')[-1]}.mp4"

    # Sanitize the filename
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', '_', filename)

    # Ensure the 'videos' directory exists
    os.makedirs('videos', exist_ok=True)

    print(f"Original filename: {filename}")
    print(f"Sanitized filename: {sanitized_filename}")

    # Write the file (this is just a placeholder for actual download logic)
    with open(sanitized_filename, "wb") as f:
        f.write(b"Fake video data")  # Replace with actual video data
