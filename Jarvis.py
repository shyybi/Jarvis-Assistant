import speech_recognition as sr
from gtts import gTTS
import datetime
import os
from youtubesearchpython import VideosSearch

recognizer = sr.Recognizer()

voiceLang = 'en-US' # For FRENCH : fr-FR, For English en-US

def voice_capture():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio


def search_and_play_video(query):
    videos_search = VideosSearch(query, limit = 1)
    results = videos_search.result()
    if results['result']:

        video_url = results['result'][0]['link']
        response = "Playing video : " + results['result'][0]['title'] 
        language = 'en'
        myobj = gTTS(text=response, lang=language, slow=False)
        myobj.save("reponse.mp3")
        os.system("ffplay -nodisp -autoexit reponse.mp3")
        os.system(f"start {video_url}")
    else:
        response = "Video not found"
        language = 'en'
        myobj = gTTS(text=response, lang=language, slow=False)
        myobj.save("reponse.mp3")
        os.system("ffplay -nodisp -autoexit reponse.mp3")



def Jarvis(audio):
    try:
        output = recognizer.recognize_google(audio, language=voiceLang)
        print("You said: " + output)

        if output.startswith("Jarvis"):
            if "video" in output:
                query = output[12:]
                search_and_play_video(query)
            elif "play" in output:
                query = output[15:]
                search_and_play_video(query)
            if "time" in output:
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                response = "It's" + current_time
                language = 'en'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")

            if "start" in output:
                response = f"Starting service : {output[13:]}"
                language = 'en'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")
                os.system(f"start {output[13:]}")

            if "stop" in output:
                response = f"Stopping service : {output[14:]}"
                language = 'en'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")
                os.system(f"taskkill /f /im {output[14:]}")
            

    except sr.UnknownValueError:
        text = ""
        print("Sorry, I don't understand what you said.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))     

def main():
    while True:
        audio = voice_capture()
        output = Jarvis(audio)
    
if __name__ == "__main__":
    main()