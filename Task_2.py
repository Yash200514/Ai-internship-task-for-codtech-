import speech_recognition as sr 

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            print("Listening to audio file...")
            audio_data = recognizer.record(source)

            print("Converting speech to text...")
            text = recognizer.recognize_google(audio_data)

            return text

    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio."

    except sr.RequestError:
        return "Could not request results from the speech service."


def main():
    print("---- Speech to Text System ----")

    file_name = input("Enter audio file name (example: audio.wav): ")

    result = speech_to_text(file_name)

    print("\nTranscribed Text:\n")
    print(result)


if __name__ == "__main__":
    main()
