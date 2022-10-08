#python -m pip install --upgrade pip
# pip install gTTS
# pip install playsound



from gtts import gTTS
from playsound import playsound

text = 'Hello world'
var = gTTS(text=text, lang='en')
var.save('eng.mp3')
playsound('.\eng.mp3')