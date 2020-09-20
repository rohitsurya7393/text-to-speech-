from gtts import gTTS
from playsound import playsound
##audio='new.mp3'
##tobeconverted=input("enter text")
filename=input("enter file name")
handle=open(filename)
for line in handle:
	word=line.split()
length=len(word)
for i in range (0,length):
	vo=gTTS(text=word[i],lang='en',slow=False)
	vo.save('new{0}.mp3'.format(i))
	playsound('new{0}.mp3'.format(i))

	



    
