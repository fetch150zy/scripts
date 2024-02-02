import cv2
import os
from moviepy.editor import *


def images_to_video(image_folder, output_video_file, fps, music_file):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    temp_video_file = "temp_" + output_video_file
    video = cv2.VideoWriter(temp_video_file, fourcc, fps, (width, height))

    for image in images:
        img = cv2.imread(os.path.join(image_folder, image))
        resized_img = cv2.resize(img, (width, height))
        video.write(resized_img)

    video.release()

    video_clip = VideoFileClip(temp_video_file)
    audio_clip = AudioFileClip(music_file)
    video_duration = video_clip.duration
    audio_duration = audio_clip.duration

    if audio_duration > video_duration:
        audio_clip = audio_clip.subclip(0, video_duration)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_video_file, codec='libx264', audio_codec='aac')

    if os.path.exists(temp_video_file):
        os.remove(temp_video_file)


def main():
    image_folder = '/home/fetch150zy/Pictures/Camera/'
    output_video_file = 'video_with_music.mp4'
    fps = 2
    music_file = 'summertime.mp3'
    images_to_video(image_folder, output_video_file, fps, music_file)


if __name__ == '__main__':
    main()