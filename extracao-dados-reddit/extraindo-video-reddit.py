# Salvando vídeos.

import praw
import os
import moviepy as mpe
import requests
import re


with open('senha reddit.txt', 'r') as f:
    minha_senha = f.read()

with open('reddit client id.txt', 'r') as g:
    client_key = g.read()

with open('reddit client secret.txt', 'r') as h:
    client_secret = h.read()

headers = {'User-Agent':'windows:script for automation:v0.1 (by u/RevolutionaryLab7729'}

# -------------------------------------------------------------------------------------------------

reddit_instance = praw.Reddit(client_id= client_key,
                              client_secret = client_secret,
                              password = minha_senha,
                              user_agent = headers,
                              username = "RevolutionaryLab7729")

next_level_instance = reddit_instance.subreddit('nextfuckinglevel')

hot = next_level_instance.hot(limit=1)

output_folder = 'videosAPI'


def get_video_url(submission):

	if submission.is_video == False:
		return None

	# Checa se postagem tem URL do vídeo.
	if (not submission.media) or ('reddit_video' not in submission.media) or ('fallback_url' not in submission.media['reddit_video']):
		return None


	url_video = re.search(r"https://v.redd.it/\w+/\w+.mp4", submission.media['reddit_video']['fallback_url'])

	if not url_video:
		return None


	return url_video.group(0)

'''
Para fazer o download do vídeo, temos que baixá-lo e baixar o áudio dele.
Para acessar a URL do áudio, transformamos a URL do vídeo para o seguinte formato:
https://v.redd.it/{id}/DASH_AUDIO_{samplerate}.mp4
Por padrão, vamos usar samplerate = 128.
'''

def download_video(reddit_video_url, output_folder, output_name):

	video_file_name = f"{output_folder}/temp_video.mp4"
	audio_file_name = f"{output_folder}/temp_audio.mp4"

	output_file_name = f"{output_name}.mp4"

	audio_url = re.sub(r'/DASH_\d+\.mp4', '/DASH_AUDIO_128.mp4', reddit_video_url)

	with open(video_file_name, 'wb') as video_file:
		video_file.write(requests.get(reddit_video_url).content)

	with open(audio_file_name, 'wb') as audio_file:
		audio_file.write(requests.get(audio_url).content)

	video_clip = mpe.VideoFileClip(video_file_name)
	audio_clip = mpe.AudioFileClip(audio_file_name)

	video_clip.audio = audio_clip.subclipped(0,video_clip.duration)

	video_clip.write_videofile(f"{output_folder}/{output_file_name}",fps=30, audio_codec="aac", audio_bitrate="128k")
	os.remove(video_file_name)
	os.remove(audio_file_name)
	

for submission in hot:
	
	video_url = get_video_url(submission)

	if video_url is not None:
		download_video(video_url, output_folder, submission.title)
