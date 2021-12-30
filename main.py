from mathpix.mathpix import MathPix
import numpy as np
import time
import sys
import threading
import pyperclip
import signal
import os
import keyboard   
from PIL import ImageGrab
import json
app_id = ""
app_key = ""
with open("app.json", "r") as st_json:
    data = json.load(st_json)
    app_id=data['app_id'] 
    app_key=data['app_key'] 

def key_callback():
    print("변환 시작!")
    try:
        ocr = mathpix.process_image(image_path="data.png")
        print("=======================Latex변환=========================")
        print(ocr.latex)
        print("=========================================================")
        print("정확도 : ",ocr.latex_confidence)
        pyperclip.copy(ocr.latex)
        print("클립보드 COPY 완료")
    except:
        print("Mathpix Error");
keyboard.add_hotkey('ctrl+shift+a', key_callback)

is_running = 1;
new_data = 0;
mathpix = MathPix(app_id=app_id, app_key=app_key)
img = np.zeros((100,100),dtype=np.uint8);
def handler(signum, frame):
    global is_running
    is_running = 0
    print("프로그램 종료.")
def check_clipboard():
    global is_running
    global img
    global new_data
    im = ImageGrab.grabclipboard();
    prev_im_shape=np.array(im).shape
    while(is_running):
        im = ImageGrab.grabclipboard();
        im_shape = np.array(im).shape
        if(prev_im_shape!=im_shape and len(prev_im_shape)<=len(im_shape)):
            os.system('cls||clear')
            img = np.array(im);
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("새로운 이미지 획득",current_time)
            try:
                im.save('data.png')
                print("이미지 저장")
            except:
                pass
            time.sleep(1)
        prev_im_shape=im_shape
        time.sleep(1)
if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    print("프로그램 시작")
    t1 = threading.Thread(target=check_clipboard)
    t1.start()
    while(is_running):

        time.sleep(0.1)
