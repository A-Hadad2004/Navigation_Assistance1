def main():
    print("אתה כאן")
    import pyttsx3
    engine = pyttsx3.init()
    engine.say('Hello, you have arrived the: orientation in the environment, say the name of the object you would like to find')
    engine.runAndWait()
    print("you hear")
    engine.say('The objects that we can, detect for you are: bed, table, chair, library, closet, dresser, coffee table and sofa')
    engine.runAndWait()
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

