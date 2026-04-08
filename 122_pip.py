#findout python package to convert english text into gujarati text and use it
import asyncio
from googletrans import Translator

async def translate_text():
    translator = Translator()
    
    text = "Hello, how are you?"
    
    translated = await translator.translate(text, src='en', dest='gu')
    
    print("Original:", text)
    print("Gujarati:", translated.text)

# Run async function
asyncio.run(translate_text())