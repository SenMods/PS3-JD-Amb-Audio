import os
try:
	os.mkdir('output/')
	os.mkdir('input/')
except:
	pass	
print('''
DISCLAMER
I do not own any of this code. I just edited the header part and folder making.
All the credits of this code go to RyanL181095 and JackLSummer15.

''')

input('Press any key to continue')


os.makedirs('output/temp', exist_ok=True)

for audio in os.listdir("input/"):
	audioname=audio.replace(".webm","").replace(".mpeg","").replace(".flv","").replace(".mp4","").replace(".avi","").replace(".wmv","").replace(".aac","").replace(".m4a","").replace(".wma","").replace(".ogg","").replace(".mp3","").replace(".wav","")+'.mp3'
	
	os.system('ffmpeg -i input/'+audio+' -write_xing 0 -id3v2_version 0 -b:a 192k -ac 2 -ar 48000 output/temp/'+audioname)
	
	with open('output/temp/'+audioname,'rb') as f:
	
		data=f.read()
		
		rakiheader=b'\x52\x41\x4B\x49\x00\x00\x00\x09\x50\x53\x33\x20\x6D\x70\x33\x20\x00\x00\x00\x48\x00\x00\x00\x80\x00\x00\x00\x02\x00\x00\x00\x00\x66\x6D\x74\x20\x00\x00\x00\x38\x00\x00\x00\x10\x4D\x73\x66\x20\x00\x00\x00\x80\x00\x03\xA5\xC0\x00\x55\x00\x02\x00\x00\xBB\x80\x00\x02\xEE\x00\x00\x04\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
	
	wavckd=open('output/'+audioname.replace(".mp3",".wav")+'.ckd','wb')
	
	wavckd.write(rakiheader+data)
	wavckd.close()
	
	os.remove('output/temp/'+audioname)
os.rmdir('output/temp')