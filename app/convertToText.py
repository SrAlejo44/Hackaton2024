import assemblyai as aai

def audioConvert(apiKey, urlAudio, urlTexto):
  # Replace with your API key
  aai.settings.api_key = apiKey

  # URL of the file to transcribe
  FILE_URL = urlAudio

  # You can also transcribe a local file by passing in a file path
  # FILE_URL = './path/to/file.mp3'

  config = aai.TranscriptionConfig(speaker_labels=True)

  transcriber = aai.Transcriber()
  transcript = transcriber.transcribe(
    FILE_URL,
    config=config
  )

  with open(urlTexto, "w", encoding="utf-8") as archivo:  # 'a' para agregar sin sobrescribir

    # Iterar sobre las frases en transcript
    for utterance in transcript.utterances:
        # Formatear el texto
        output = f"Speaker {utterance.speaker}: {utterance.text}\n"
        
        # Guardar en el archivo
        archivo.write(output)
