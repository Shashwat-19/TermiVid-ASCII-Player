import cv2
import os
import time
import numpy as np
import argparse
import shutil

def convert_frame_to_ascii(frame, width):
    """
    Convert a frame to ASCII art using a character set based on brightness
    """
    ascii_chars = " .:-=+*#%@"
    height = int(frame.shape[0] * width / frame.shape[1] / 2)
    height = max(1, height)

    resized_frame = cv2.resize(frame, (width, height))
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    normalized = gray_frame / 255.0
    ascii_frame = ""
    for row in normalized:
        for pixel in row:
            index = int(pixel * (len(ascii_chars) - 1))
            ascii_frame += ascii_chars[index]
        ascii_frame += "\n"
    return ascii_frame, height, width

def play_video_in_terminal(video_path, fps=30):
    if not os.path.exists(video_path):
        print(f"Error: Video file '{video_path}' not found.")
        return
    
    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1.0 / video_fps if video_fps > 0 else 1.0 / fps

    # Get terminal size
    cols, rows = shutil.get_terminal_size()
    # Leave a margin so it looks nicer
    max_width = max(10, cols - 10)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Auto-resize ASCII width to fit terminal
            ascii_art, ascii_height, ascii_width = convert_frame_to_ascii(frame, width=max_width)

            # Calculate vertical and horizontal padding
            top_padding = max(0, (rows - ascii_height) // 2)
            left_padding = " " * max(0, (cols - ascii_width) // 2)

            os.system('cls' if os.name == 'nt' else 'clear')

            # Print with padding
            print("\n" * top_padding, end="")
            for line in ascii_art.splitlines():
                print(left_padding + line)

            time.sleep(frame_delay)

    except KeyboardInterrupt:
        print("\nVideo playback interrupted.")
    finally:
        cap.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play a video as ASCII in the terminal.")
    parser.add_argument("video_path", help="Path to the video file")
    args = parser.parse_args()

    play_video_in_terminal(args.video_path)