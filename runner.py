from main import MainSetUp

# Runner

main = MainSetUp()

web_browser = main.browser

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
            if "open" in text:
                if num != -1:  # browser is already opened
                    num = -1
                    main.browser.driver.close()

                web_browser.run(text)
                num = 0  # opening a browser
            elif "close browser" in text:
                main.browser.driver.close()
                num = -1
            elif "stop" in text:
                print("\033[1;32;40m [Kanna-Chan]: Goodbye")
                main.speak("Goodbye")
                exit()

    elif "stop" in text:
        print("\033[1;32;40m [Kanna-Chan]: Bruh, you just started it")
        main.speak("Bruh, you just started it")
        exit()
