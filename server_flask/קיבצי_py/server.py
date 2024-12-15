import torch
import speech_recognition as sr
import pyttsx3
import os
import cv2
from flask import Flask, render_template, request
from flask_cors import cross_origin
print("היי")
# הגדרת מודול זיהוי דיבור ויולו
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# טעינת המודל פעם אחת בעת הפעלת השרת
model = torch.hub.load('ultralytics/yolov5', 'custom', path='../best.pt', force_reload=True)

# ייבוא הפונקציות שלך מקבצים נפרדים
from main_function import *
from Distance_calculation import *
from Detection import *
from shoot_a_frame import *
from Voice import *

app = Flask(__name__)

# דף הבית
@app.route('/')
def hello():
    return render_template('fronted.html')

# נתיב לקבלת בקשות GET
@app.route('/get', methods=['GET'])
@cross_origin()
def get_request():
    try:
        # קריאה לפונקציה הראשית שלך
        main()
        return render_template('fronted.html')
    except Exception as e:
        # החזרת הודעת שגיאה במידה ומשהו נכשל
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)