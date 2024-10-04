import speech_recognition as sr
from gtts import gTTS
import datetime
import os
from youtubesearchpython import VideosSearch

recognizer = sr.Recognizer()

voiceLang = 'fr-FR' # For FRENCH : fr-FR, For English en-US

def voice_capture():
    with sr.Microphone() as source:
        print("Écoute...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        recognizer.adjust_for_ambient_noise(source)
    return audio


def search_and_play_video(query):
    videos_search = VideosSearch(query, limit = 1)
    results = videos_search.result()
    if results['result']:

        video_url = results['result'][0]['link']
        response = "Lecture de la vidéo : " + results['result'][0]['title'] 
        language = 'fr'
        myobj = gTTS(text=response, lang=language, slow=False)
        myobj.save("reponse.mp3")
        os.system("ffplay -nodisp -autoexit reponse.mp3")
        os.system(f"start {video_url}")
    else:
        response = "Aucune vidéo trouvée pour la recherche."
        language = 'fr'
        myobj = gTTS(text=response, lang=language, slow=False)
        myobj.save("reponse.mp3")
        os.system("ffplay -nodisp -autoexit reponse.mp3")



def Jarvis(audio):
    try:
        output = recognizer.recognize_google(audio, language=voiceLang)
        print("Vous avez dit: " + output)
        
        if output.startswith("Jarvis"):
            if "vidéo" in output:
                query = output[12:]
                search_and_play_video(query)

            elif "joue" in output:
                query = output[15:]
                search_and_play_video(query)

            elif "mets" in output:
                query = output[15:]
                search_and_play_video(query)
            if "heure" in output:
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                response = "Il est " + current_time
                language = 'fr'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")

            if "lance" in output:
                response = f"Démarrage du service : {output[13:]}"
                language = 'fr'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")
                os.system(f"start {output[13:]}")
                os.system("exit")
            
  
            
            if "arrête" in output:
                response = f"Arrêt du service : {output[14:]}"
                language = 'fr'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")
                os.system(f"taskkill /f /im {output[14:]}.exe")


            if "arrête la musique" in output:
                response = f"Arrêt de la musique"
                language = 'fr'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")
                os.system(f"taskkill /f /im firefox.exe")


            if "suicider" in output:
                response = f"Bah arrete"
                language = 'fr'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")
                
            if "comment tu vas" in output:
                response = f"Tranquille ecoute le sang"
                language = 'fr'
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("reponse.mp3")
                os.system("ffplay -nodisp -autoexit reponse.mp3")


    except sr.UnknownValueError:
        text = ""
        print("Désolé, je n'ai pas compris.")
    except sr.RequestError as e:
        text = ""
        print("Erreur; {0}".format(e))     

def main():
    while True:
        audio = voice_capture()
        output = Jarvis(audio)
    
if __name__ == "__main__":
    main()