import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen for user input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

# Define a main function to run the voice assistant
def main():
    speak("Hello, how can I assist you today?")
    query = listen()

    # Use if-else statements to perform specific actions based on user input
    if 'play' in query.lower():
        song = query.replace('play', '')
        pywhatkit.playonyt(song)
    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    elif 'who is' in query.lower():
        person = query.replace('who is', '')
        info = wikipedia.summary(person, sentences=2)
        speak(info)
    else:
        speak("I'm sorry, I didn't understand that.")

# Run the main function
if __name__ == "__main__":
    main()