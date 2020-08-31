import speech_recognition as sr


# Passes in audio to the application for comparison with a random word, an external module (from google) is used here
def recognise_speech(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        response = {
            "Success": True,
            "Error": None,
            "transcription": None
        }
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["Success"] = False
            response["Error"] = "API unavailable"
        except sr.UnknownValueError:

            # speech was unintelligible
            response["Error"] = "Unable to recognize speech"

        return response