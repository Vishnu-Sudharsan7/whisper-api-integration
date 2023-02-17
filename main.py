import os
import subprocess

import requests
#
# import whisper
# def transcript():
#     model = whisper.load_model("base")
#     result = model.transcribe("C:/Users/vishn/PycharmProjects/pythonProject5/sam.mp3")
#     print(result["text"])
# transcript()
#
#
# import whisper
#
# model = whisper.load_model("base.en")
# audio = "C:/Users/vishn/PycharmProjects/pythonProject5/sam.mp3"
# subprocess.call(["ffmpeg","-y","i",audio,],
#                 stdout=subprocess.DEVNULL,
#                 stderr=subprocess.STDOUT,
#                 shell=True
# )
# fileexists = os.path.isfile(audio)
# print(fileexists)
# result=model.transcribe(audio)
# #result = model.transcribe(audio, fp16=False, language="en")

#
# import whisper
#
# model = whisper.load_model("base")
#
# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("sam.wav")
# audio = whisper.pad_or_trim(audio)
#
# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)
#
# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")
#
# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)
#
# # print the recognized text
# print(result.text)

from flask import Flask, jsonify, request
import whisper
app = Flask(__name__)

@app.route('/api',methods=['GET'])
def index():
    #def transcript():
    model = whisper.load_model("base")
    result = model.transcribe("C:/Users/vishn/PycharmProjects/pythonProject5/sam.mp3")
    print(result["text"])
    return jsonify(result['text'])
@app.route('/api2',methods=['POST'])


def req():
    request_data = request.get_json()
    print(request_data)
    model = whisper.load_model("base")
    result = model.transcribe("C:/Users/vishn/PycharmProjects/pythonProject5/sam.mp3")
    print(result["text"])
    return jsonify(result['text'])


app.run(host='0.0.0.0', port=81)