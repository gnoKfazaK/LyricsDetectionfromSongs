import whisper
from bot import MODEL_SIZE

def load_model_whisper():
    model = whisper.load_model(MODEL_SIZE)

    print('Whisper model loaded')
    return model

def get_lyrics(model, file):
    print('Transcribing...')
    lyrics = model.transcribe(file)
    print('Transcribed')
    return lyrics['text']

