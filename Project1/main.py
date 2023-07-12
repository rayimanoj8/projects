import random

import AppOpener

import win32com.client
import speech_recognition as sr
import openai
import webbrowser

apps = AppOpener.give_appnames()
print('spotify' in apps)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
chatStr = ""
c = open("chat" + str(random.randint(0, 12321312)) + "txt", 'a')


def chat(query):
    global chatStr
    c.write(chatStr)
    print(chatStr)
    openai.api_key = "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"
    chatStr += f"Manoj : {query}\n babu : "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def say(text):
    speaker.Speak(text)


def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        return query


if __name__ == '__main__':
    print('PyCharm')
    say("Listening...")
    print("Listening...")
    while True:
        text = take().lower()
        print(text)
        if "play" in text:
            text=text[5:-4]
            import pyautogui
            import os
            import time
            os.system("spotify")
            time.sleep(5)
            pyautogui.hotkey("ctrl", 'l')
            pyautogui.write(text, interval=0.1)
            for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
                time.sleep(2)
                pyautogui.press(key)
        # sites={"youtube":'"https://youtube.com"',
        #        "instagram":"https://instagram.com",
        #        "google":"https://google.com"
        #        }
        # for i in sites:
        #     if f"open {i}" in text.lower():
        #         webbrowser.open(sites[i])
        #         say(f"Opening {i} sir")
        elif "open" in text:
            cmd = "".join(text.split("open "))
            print(cmd)
            if cmd in apps:
                AppOpener.open(cmd)
                say("opening " + cmd)
                exit()
            else:
                webbrowser.open("https://" + cmd + ".com")
                say("opening " + cmd + ".com")
                exit()
        else:
            chat(text)