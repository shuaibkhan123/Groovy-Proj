import pafy
import vlc
import os
import time


url = "#vid_url"
video = pafy.new(url)
best_audio=video.getbestaudio()
playurl=best_audio.url

Instance = vlc.Instance()
Media = Instance.media_new(playurl)
player = Instance.media_player_new()
player.set_media(Media)
player.set_mrl(playurl,":no-video")
player.play()


while True:
	pass
