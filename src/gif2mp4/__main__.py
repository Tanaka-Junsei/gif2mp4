import os
import shutil
from moviepy.editor import VideoFileClip

def copy_input_to_output(input_dir, output_dir):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    shutil.copytree(input_dir, output_dir)

def convert_gif_to_mp4(gif_path, mp4_path):
    print(f"Converting: {gif_path} -> {mp4_path}")
    try:
        clip = VideoFileClip(gif_path)
        clip.write_videofile(mp4_path, codec="libx264", audio=False)
        clip.close()
    except Exception as e:
        print(f"Error converting {gif_path}: {e}")

def main():
    input_dir = "input"
    output_dir = "output"
    
    copy_input_to_output(input_dir, output_dir)
    
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.lower().endswith(".gif"):
                gif_path = os.path.join(root, file)
                base_name = os.path.splitext(file)[0]
                mp4_file = base_name + ".mp4"
                mp4_path = os.path.join(root, mp4_file)
                
                convert_gif_to_mp4(gif_path, mp4_path)
                
                os.remove(gif_path)
                print(f"Deleted original file: {gif_path}")

if __name__ == "__main__":
    main()
