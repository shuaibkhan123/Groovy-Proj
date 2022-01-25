import pafy
import vlc
import os
import time
import urllib.request
import msic_streamer as ms

state=0
def song_play(song_name):
	global player
	results=ms.play_song(song_name)
	#o_s="https://www.youtube.com/watch?v=3Tnf9AxEtnc"
	url =results[1]
	video = pafy.new(url)
	best_audio=video.getbestaudio()
	playurl=best_audio.url
	Instance = vlc.Instance()
	Media = Instance.media_new(playurl)
	player = Instance.media_player_new()
	player.set_media(Media)
	player.set_mrl(playurl,":no-video")




def ply():
	global player
	global state
	if(state==0):
		player.play()
		state=1
		print("started playing")
		a=player.is_playing()
		print(a)
	else:
		if(state==1):
			player.pause()
			state=-1
			print("paused")
			a=player.is_playing()
			print(a)
		else:
			player.play()
			state=1
			print("resumed")
			a=player.is_playing()
			print(a)


def sttop():
	global state
	state=0
	player.stop()
	print("stopped")
	a=player.is_playing()
	print(a)


















"""code = urllib.request.urlopen(url).getcode()
if str(code).startswith('2') or str(code).startswith('3'):
    print('Stream is working')
else:
    print('Stream is dead')"""

"""good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
while str(player.get_state()) in good_states:
    #print('Stream is working. Current state = {}'.format(player.get_state()))
    player.pause()

print('Stream is not working. Current state = {}'.format(player.get_state()))
player.stop()"""