def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio


def convert_voice_to_text(audio):
    try:
        # text = recognizer.recognize_sphinx(audio)
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text


def sending_the_cl(cl):
    import pyttsx3
    engine = pyttsx3.init()
    """the function get the name of the class and sending it to the make_frame function
    and the make_frame function will send to the detect function"""
    engine.say("we want to take a fram of your environment.")
    engine.runAndWait()
    frame_Capture(cl)


def process_voice_command(text):
    import pyttsx3
    engine = pyttsx3.init()
    if "hello" in text.lower():
        # print("Hello! How can I help you?")
        engine.say('Hello, How can I help you')
        engine.runAndWait()
    elif "bed" in text.lower():
        engine.say('the object you search for is a bed')
        engine.runAndWait()
        sending_the_cl("0")
    elif "coffee" in text.lower() and "table" in text.lower():
        engine.say('the object you search for is a coffee table')
        engine.runAndWait()
        sending_the_cl("7")
    elif "table" in text.lower():
        engine.say('the object you search for is a table')
        engine.runAndWait()
        sending_the_cl("1")
    elif "sofa" in text.lower():
        engine.say('the object you search for is a sofa')
        engine.runAndWait()
        sending_the_cl("2")
    elif "dresser" in text.lower():
        engine.say('the object you search for is a dresser')
        engine.runAndWait()
        sending_the_cl("3")
    elif "chair" in text.lower() or "ch" in text.lower() or "Find" in text.lower():
        engine.say('the object you search for is a chair')
        engine.runAndWait()
        sending_the_cl("0")
    elif "closet" in text.lower():
        engine.say('the object you search for is a closet')
        engine.runAndWait()
        sending_the_cl("5")
    elif "library" in text.lower():
        engine.say('the object you search for is a libary')
        engine.runAndWait()
        sending_the_cl("6")
    elif "close" in text.lower():
        engine.say("Goodbye! Have a great day!")
        engine.runAndWait()
        return True
    else:
        # print("I didn't understand that command. Please try again.")
        engine.say('I didnt understand that command. Please try again.')
        engine.runAndWait()
    return False


