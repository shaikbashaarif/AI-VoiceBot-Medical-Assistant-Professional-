# step1a: setup Text to speech-TTS-model with gTTS
import os
from gtts import gTTS
import elevenlabs
from elevenlabs import ElevenLabs
import subprocess
import platform

def text_to_speech_with_gtts_old(input_text,output_filepath):
    language='en'
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False

    )
    audioobj.save(output_filepath)

input_text = 'Hi this is AI with Arif'
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")


# step1b: setup Text to speech-TTS-model with Elevenlabs
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    audio = client.generate(
        text=input_text,
        voice="Aria",
        model="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="eleven_testing.mp3")
# step2: setup model for text output to voice

def text_to_speech_with_gtts(input_text,output_filepath):
    language='en'
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False

    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text = 'Hi this is AI with Arif, autoplay testing'
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    audio = client.generate(
        text=input_text,
        voice="Aria",
        model="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


text_to_speech_with_elevenlabs(input_text, output_filepath="eleven_testing_autoplay.mp3")