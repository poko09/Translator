import sounddevice as sd
from scipy.io.wavfile import write
import whisper


class Translator:

    def __init__(self):
        self.model = whisper.load_model("base")

    def record_audio(self):
        # Sampling frequency
        freq = 44100

        # Recording duration
        duration = 15
        # Start recorder with the given values
        # of duration and sample frequency
        print("Recording audio... ")
        recording = sd.rec(int(duration * freq),
                           samplerate=freq, channels=1)
        # Record audio for the given number of seconds
        sd.wait()
        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write("recording2.wav", freq, recording)

        print("Nagranie zakończone!")

    def transcribe_text(self, audio_file):
        model = whisper.load_model('base')
        result = self.model.transcribe(audio_file, fp16=False)
        return result['text']

    def translate_text(self, audio_file):
        result = self.model.transcribe(audio_file, fp16=False, task='translate')
        return result['text']

    def detect_language(self, audio_file):
        audio = whisper.load_audio(audio_file)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        _, probs = self.model.detect_language(mel)
        return (f"Wykryty język to: {max(probs, key=probs.get)}")

