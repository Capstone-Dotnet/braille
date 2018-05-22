# -*- coding: utf-8 -*-
"""
     *******************   이슈    ************************
tts 관련해서 네이버 구글 아마존 검색결과 
인터넷이 연결된 환경에서 가능한거 같습니다.
 
pyttsx3 (영어밖에 지원 안하는듯...  남여 목소리변경 rate변경 확인 ...)
# 패키지 설치 
# pip install pyttsx로 또는 sudo pip install pyttsx   파이썬 버전 확인 필요.    
# pip install pyttsx3 2.7 ~ 3.6까지 동작한다고 함.. 
# pip install pypiwin32

# pyttsx3 사용예제
engine = pyttsx3.init()  
engine.setProperty('rate', 150) 
engine.say('Greetings!') 
engine.say('How are you today?' ) 
engine.runAndWait()   

"""
# import RPi.GPIO as GPIO
import time
# import pyttsx3
import random   
# import pygame
from mock_braille_controller import SolenoidController
from mock_braille_controller import AnswerReader
import mock_sound_controller



# 전역변수  
play_mode = 0 # 교육:1 / 문제:2
language_selection = 0 # 언어선택   
english = [[0],[0,2],[0,1],[0,1,3],[0,3],[0,1,2],[0,1,2,3],[0,2,3],[1,2],[1,2,3],[0,4],[0,2,4],[0,1,4],[0,1,3,4],[0,3,4],[0,1,2,4],[0,1,2,3,4],[0,2,3,4],[1,2,4],[1,2,3,4],[0,4,5],[0,2,4,5],[1,2,3,5],[0,1,4,5],[0,1,3,4,5],[0,3,4,5]] # A~Z
hangle_front = [[1],[0,1],[1,2],[3],[0,3],[1,3],[5],[0,1,2,3],[1,5],[3,5],[0,1,2],[0,2,3],[0,1,3],[1,2,3]] # ㄱ~ ㅎ
hangle_middle = [[0,2,5],[1,3,4],[1,2,4],[0,3,5],[0,4,5],[1,4,5],[0,1,4],[0,1,5],[1,2,5],[0,3,4],[0,2,3,4],[0,1,3,4]] #ㅏ,ㅑ,ㅓ,ㅕ,ㅗ,ㅛ,ㅜ,ㅠ,ㅡ,ㅣ,ㅐ,ㅔ
hangle_end = [[0],[2,3],[3,4],[2],[2,5],[0,2],[4],[2,3,4,5],[0,4],[2,4],[2,3,4],[2,4,5],[2,3,5],[3,4,5]] # ㄱ~ㅎ
sript = [ 'Select Play mode' , 'Select Play language' ]

def main():
    global play_mode
    global language_selection
    talker('Select play mode')
    play_mode = input("Select Play mode (edu:0 or quize:1) : ") #button 실행모드확인
    talker('Select Play language')
    language_selection = input("Select Play language (english:0 or hangle:1) : ") #button 언어확인

    # 1 교육모드
    if play_mode == 0:
        print('Start Edu!')
        talker('Start edu')

        if language_selection == 0:       #영어 시작
            print('English start')
            english_edu()
        else:                             #한글 시작
            print('hangle start')
            hangle_edu()

    # 2 문제모드
    else:
        print('Start Quize!')
        talker('Start quize')

        if language_selection == 0:       #영어 시작
            print('English start')
            english_quize()
        else:                             #한글 시작
            print('hangle start')
            hangle_quize()

def talker(string):
    time.sleep(2)
    # engine = pyttsx3.init() # tts init
    # engine.setProperty('rate', 100)
    # engine.say(string)
    # engine.runAndWait()

def english_edu():
    solenoid = SolenoidController()

    # 버튼 출력
    for i in range(len(english)):
        button_up = english[i]
        for j in range(len(button_up)):
            solenoid.on(button_up[j])

        # 스피커 출력
        mock_sound_controller.play_sound()
        time.sleep(2.0)

        # 버튼확인 및 버튼 초기화 (로직이 정지했다가 확인버튼이 입력되면 다음 명령 실행?)
        talker('Solenoid check')
        print('Solenoid check')
        pause = input() # 확인버튼값을 받아야함

        if  pause == True :
            print('Next dictionary')

def hangle_edu():
    solenoid = SolenoidController()

    #버튼 출력(초성)
    for i in range(len(hangle_front)):
        button_up = hangle_front[i]
        for j in range(len(button_up)):
            solenoid.on(button_up[j])

        #스피커 출력
        mock_sound_controller.play_sound()
        time.sleep(2.0)

        #버튼확인 및 버튼 초기화
        talker('Solenoid check')
        print('Solenoid check')
        pause = input()  # 확인버튼값을 받아야함

        if pause == True:
            print('Next dictionary')

    #버튼 출력(중성)
    for i in range(len(hangle_middle)):
        button_up = hangle_middle[i]
        for j in range(len(button_up)):
            solenoid.on(button_up[j])

         # 스피커 출력
        mock_sound_controller.play_sound()
        time.sleep(2.0)

         # 버튼확인 및 버튼 초기화
        talker('Solenoid check')
        print('Solenoid check')
        pause = input()  # 확인버튼값을 받아야함

        if pause == True:
            print('Next dictionary')

    #버튼 출력(종성)
    for i in range(len(hangle_end)):
        button_up = hangle_end[i]
        for j in range(len(button_up)):
            solenoid.on(button_up[j])

        #스피커 출력
        mock_sound_controller.play_sound()
        time.sleep(2.0)

        #버튼확인 및 버튼 초기화
        talker('Solenoid check')
        print('Solenoid check')
        pause = input()  # 확인버튼값을 받아야함

        if pause == True:
            print('Next dictionary')

def english_quize():

    for i in range(len(english)):
        problem = english[random.randint(1,26)] #문제

        # 스피커 출력
        mock_sound_controller.play_sound()
        time.sleep(2.0)

        answer = input() # 정답입력 받고

        # if  == :  #정답확인
        #     talker('success')
        #     print('success')
        #
        # else:
        #     talker('fail')
        #     print('fail')

def hangle_quize():

    for i in range(len(english)):
        problem = english[random.randint(1,26)] #문제
    #
    #     # 스피커 출력
        mock_sound_controller.play_sound()
    #     time.sleep(2.0)
    #
    #     answer = input() # 정답입력 받고
        #
        # if  == :  #정답확인
        #     talker('success')
        #     print('success')
        #
        # else:
        #     talker('fail')
        #     print('fail')

main()