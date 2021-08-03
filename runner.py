from main import MainSetUp
from colors import COLOR
from browser_websites import Browser

# Runner

main = MainSetUp()
web_browser = Browser()

print(COLOR.GREEN + "[Kanna-Chan]: Start up successful")
main.speak("Start up successful")

# the actual input code
while True:
    text = main.get_audio()
    text.lower()

    print(text)  # temporary solution

    if "computer" in text:
        print(COLOR.GREEN + "[Kanna-Chan]: Hello Sir")
        main.speak("Hello Sir")

        while True:
            text = main.get_audio()
            text.lower()

            print(text)  # temporary solution
            if "open" in text:
                try:
                    web_browser.run(text)
                except Exception as e:
                    print(COLOR.RED + "[Kanna-Chan]: Could not open browser")
                    main.speak("Could not open browser")
            elif "stop" in text:
                print(COLOR.GREEN + "[Kanna-Chan]: Goodbye")
                main.speak("Goodbye")
                exit()

    elif "stop" in text:
        print(COLOR.RED + "[Kanna-Chan]: Bruh, you just started it")
        main.speak("Bruh, you just started it")
        exit()
