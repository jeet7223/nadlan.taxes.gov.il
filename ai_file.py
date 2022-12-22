#!/usr/bin/env python3
import glob
import os

import speech_recognition as sr

import configuration


def getCaptchaText():
    try:
        list_of_files = glob.glob(configuration.captcha_path + "*")
        latest_file = max(list_of_files, key=os.path.getctime)
        latest_file = latest_file.split('/')
        latest_file = latest_file[len(latest_file) - 1]
        src_audio =  configuration.captcha_path+latest_file

    except:
        return False
    try:
        r = sr.Recognizer()
        with sr.AudioFile(src_audio) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
    except:
        pass
        text = None

    try:
        os.remove(src_audio)
    except:
        pass
    return text

