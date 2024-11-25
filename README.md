# Prototipo de Aplicación Web - Análisis de Llamadas con AssemblyAI y LLaMA 3.1

Este repositorio contiene un prototipo de aplicación web que utiliza inteligencia artificial (IA) para convertir audio de reuniones en texto y luego procesar ese texto para extraer ideas principales, generar tareas y resúmenes de reuniones. Utilizamos la API de AssemblyAI para la transcripción de audio y la IA LLaMA 3.1 de Meta para analizar y organizar la información.

## Tecnologías Utilizadas

- **AssemblyAI**: API que convierte archivos de audio en texto. En este prototipo, se utiliza para transcribir llamadas grabadas en formato `.mp3`.
- **LLaMA 3.1 (Meta)**: Modelo de IA que procesa el texto transcrito de las llamadas, analizando el contenido y extrayendo las ideas principales, tareas y resúmenes de la reunión.
- **Python**: Lenguaje de programación utilizado para desarrollar el script que integra las APIs y el procesamiento de los datos.

## Funcionamiento

### 1. **Conversión de Audio a Texto con AssemblyAI**

Se utiliza la API de AssemblyAI para convertir los archivos de audio de las reuniones en texto. El script de `assemblyai.py` hace uso de la siguiente función para realizar la transcripción:

```python
import assemblyai as aai

def audioConvert(apiKey, url):
    # Configuración de la API
    aai.settings.api_key = apiKey

    # URL del archivo a transcribir
    FILE_URL = url

    config = aai.TranscriptionConfig(speaker_labels=True)

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL, config=config)

    # Guardar el texto transcrito
    with open("Meet.txt", "w", encoding="utf-8") as archivo:
        for utterance in transcript.utterances:
            output = f"Speaker {utterance.speaker}: {utterance.text}\n"
            archivo.write(output)
```

Este script convierte un archivo de audio proporcionado en un archivo de texto (Meet.txt), etiquetando a los hablantes y transcribiendo sus palabras.

### 2. **Análisis de Texto con LLaMA 3.1**

Una vez que el audio se ha convertido en texto, el script llama.py se encarga de enviar ese texto a la IA LLaMA 3.1 para realizar un análisis detallado. LLaMA se encarga de organizar la información en un formato JSON, que incluye el resumen de la reunión, tareas y futuras reuniones.

```python
import ollama

chat_messages = []

def create_message(content, role):
    return {'role': role, 'content': content}

def chat():
    response = ollama.chat(model='llama3', stream=True, messages=chat_messages)
    assistant_message = ''
    for chunk in response:
        assistant_message += chunk['message']['content']
        print(chunk['message']['content'], end='', flush=True)
    chat_messages.append(create_message(assistant_message, 'assistant'))

def ask(urlText):
    with open(urlText, "r", encoding="utf-8") as archivo:
        textMeet = archivo.read()

    message = f"""
    According to this meeting, fill out the fields in the json format and do not respond anything else.

    {textMeet}

    {{
    "current meet": {{
        "Meet Title": "Create a title for this meeting",
        "Current Date": "Current Date when the script execute",
        "Current Hour": "Current Hour when the script execute",
        "integrantes": [""],
        "meeting summary": "Summary this meet in one sentence"
    }},
    "task": [
        {{"Person in charge of the task": "", "Task Title":"", "task description": ""}},
        {{"Person in charge of the task": "", "Task Title":"", "task description": ""}}
    ],
    "future meet": [
        {{"Meeting name": "", "Date":"", "Meet description": ""}},
        {{"Meeting name": "", "Date":"", "Meet description": ""}}
    ]
    }}
    """
    chat_messages.append(create_message(message, 'user'))
    print(f'\n\n--{message}--\n\n')
    chat()
```

Este script procesa el archivo Meet.txt, genera un análisis detallado y lo devuelve en formato JSON.

### 3. **Configuración**

El archivo config.py contiene las claves necesarias para interactuar con las APIs de AssemblyAI y los archivos de entrada/salida:

```python
APIKEY_ASSEMBLYAI = "tu_api_key_de_assemblyai"
URL_AUDIO = "./Meet2.mp3"
URL_TEXTO = "./Meet.txt"
```

### **Requisitos**

* Python 3.13.0
* Bibliotecas necesarias:
    - assemblyai
    - ollama

Puedes instalar las dependencias utilizando pip:
```python
pip install assemblyai ollama
```

### **Uso**

1. Asegúrate de tener las claves API correctas en el archivo config.py.
2. Coloca tu archivo de audio en la carpeta correspondiente (según la variable URL_AUDIO).
3. Ejecuta el script principal para realizar la conversión y el análisis:
bash
```python
python main.py
```

Este script convertirá el audio a texto y luego analizará ese texto para generar resúmenes, tareas y reuniones futuras.

### **Contribuciones**

Si deseas contribuir a este proyecto, por favor realiza un fork y envía tus pull requests. Las contribuciones son siempre bienvenidas.