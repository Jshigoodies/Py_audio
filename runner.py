from main import MainSetUp

# Runner

main = MainSetUp()

web_browser = main.browser
driver = main.browser.driver

print("\033[1;32;40m [Kanna-Chan]: Start up successful")
main.speak("Start up successful")

# the actual input code
while True:
    text = main.get_audio()
    text.lower()

    print(text)  # temporary solution

    if "computer" in text:
        print("\033[1;32;40m [Kanna-Chan]: Hello Sir")
        main.speak("Hello Sir")

        num = -1

        while True:
            text = main.get_audio()
            text.lower()

            print(text)  # temporary solution
            if "Google" in text:
                web_browser.google()
                num = num + 1
            elif "Bing" in text:
                web_browser.bing()
                num = num + 1
            elif "stop" in text:
                print("\033[1;32;40m [Kanna-Chan]: Goodbye")
                main.speak("Goodbye")
                exit()
            else:
                print("\033[1;31;40m [Kanna-Chan]: I'm sorry, that is not a command")
                main.speak("I'm sorry, that is not a command")

    elif "stop" in text:
        print("\033[1;32;40m [Kanna-Chan]: Goodbye")
        main.speak("Goodbye")
        exit()
    else:
        print("\033[1;31;40m [Kanna-Chan]: I'm sorry, that is not a command")
        main.speak("I'm sorry, that is not a command")
