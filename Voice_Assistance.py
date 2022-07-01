# Inbuilt Libraries ============================
import speech_recognition as sr
import pyttsx3 
import webbrowser

# User defined files ============================
import Real_Time_Object_Detection as RT_detection
import Image_Window as newin


def listen():
    # Initialize the recognizer ============================
    r = sr.Recognizer() 
    
    def SpeakText(command):
        # Function to convert text to speech ============================
        
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command) 
        engine.runAndWait()
    
    # Welcome voice Note ============================
    SpeakText("Voice Assistance Activated Say a Sentence with no or deactivate to stop voice assistance")
    
    # Infinite loop to hear ============================
    while(1):    
        
        try:
            # try statement to hold exceptions ============================
            
            # use the microphone as source for input. ============================
            with sr.Microphone() as source2:
                
                print("Speak")
                #listens for the user's input 
                audio2 = r.listen(source2)
                SpeakText("Recognizing Your Words! Thank you") 
                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print(MyText)
    
                if "deactivate" in MyText or "kill" in MyText or "turn off" in MyText or "terminate" in MyText:
                    # if condition to check if their is an order to
                    # stop voice assistance
                    SpeakText("Voice Assistance Deactivated")
                    return "deactivate"
                    break

                # elif left activated
                elif "realtime" in MyText or "live"in MyText or "webcam" in MyText:
                    # checks if realtime or live as keyword in voice
                    # if found redirects to Real_Time_object_Detection file
                    SpeakText("Voice Assistanct will running in background, Webcam will be active soon") #Confirms that program will be active
                    RT_detection.start_webcam() # Initialize the file
                elif "image" in MyText or "picture" in MyText or "photo" in MyText:
                    SpeakText("Voice Assistanct will be running in background, Enter File Location in Given Box with format") #Confirms that program will be active
                    newin.create() # New window to get image location is created
                # else Speaks command not recognized/ find on google
                else:
                    # search_terms = ["hello"]
                    # for term in search_terms:
                    url = "https://www.google.com.tr/search?q={}".format(MyText)
                    webbrowser.open_new_tab(url)
                    SpeakText("Sorry, Couldn't recognize it as a command, As an assistant I have redirected you to your search result in google")

        except sr.RequestError as e:
            # holds exceptions
            # print("Could not request results; {0}".format(e))
            SpeakText("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            # holds exceptions
            # print("unknown error occured")
            SpeakText("Some Error Occured")
