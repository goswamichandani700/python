#findout ptyhon package to convert text to audio (gujarati text gujarati audio )
from gtts import gTTS

text = "નમસ્તે, કેમ છો?"
tts = gTTS(text=text, lang='gu')

tts.save("text_audio.mp3")
print("Audio file created successfully!")