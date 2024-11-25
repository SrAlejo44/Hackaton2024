from config import APIKEY_ASSEMBLYAI, URL_AUDIO, URL_TEXTO
from convertToText import audioConvert
from llamaia import ask

def main(apiKey, urlAudio, urlTexto):
    audioConvert(apiKey, urlAudio)
    ask(urlTexto)
    
main(APIKEY_ASSEMBLYAI, URL_AUDIO, URL_TEXTO)