# -*- coding: utf-8 -*-

# import RPi.GPIO as GPIO
import time
# import pyttsx3
import random
# import pygame
from mock_braille_controller import SolenoidController
from mock_braille_controller import AnswerReader
import mock_sound_controller

# 전역변수
play_mode = 0  # 교육:1 / 문제:2
language_selection = 0  # 언어선택
english = [["a", 0], ["b", 0, 2], ["c", 0, 1], ["d", 0, 1, 3], ["e", 0, 3], ["f", 0, 1, 2], ["g", 0, 1, 2, 3],
           ["h", 0, 2, 3], ["i", 1, 2], ["j", 1, 2, 3], ["k", 0, 4], ["l", 0, 2, 4], ["m", 0, 1, 4], ["n", 0, 1, 3, 4],
           ["o", 0, 3, 4], ["p", 0, 1, 2, 4], ["q", 0, 1, 2, 3, 4], ["r", 0, 2, 3, 4], ["s", 1, 2, 4],
           ["t", 1, 2, 3, 4], ["u", 0, 4, 5], ["v", 0, 2, 4, 5], ["w", 1, 2, 3, 5], ["x", 0, 1, 4, 5],
           ["y", 0, 1, 3, 4, 5], ["z", 0, 3, 4, 5]]  # A~Z
hangle_front = [[1], [0, 1], [1, 2], [3], [0, 3], [1, 3], [5], [0, 1, 2, 3], [1, 5], [3, 5], [0, 1, 2], [0, 2, 3],
                [0, 1, 3], [1, 2, 3]]  # ㄱ~ ㅎ
hangle_middle = [[0, 2, 5], [1, 3, 4], [1, 2, 4], [0, 3, 5], [0, 4, 5], [1, 4, 5], [0, 1, 4], [0, 1, 5], [1, 2, 5],
                 [0, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4]]  # ㅏ,ㅑ,ㅓ,ㅕ,ㅗ,ㅛ,ㅜ,ㅠ,ㅡ,ㅣ,ㅐ,ㅔ
hangle_end = [[0], [2, 3], [3, 4], [2], [2, 5], [0, 2], [4], [2, 3, 4, 5], [0, 4], [2, 4], [2, 3, 4], [2, 4, 5],
              [2, 3, 5], [3, 4, 5]]  # ㄱ~ㅎ
sript = ['Select Play mode', 'Select Play language']


def main():
    global play_mode
    global language_selection
    talker('Select play mode')
    play_mode = input("Select Play mode (edu:0 or quize:1) : ")  # button 실행모드확인
    talker('Select Play language')
    language_selection = input("Select Play language (english:0 or hangle:1) : ")  # button 언어확인

    # 1 교육모드
    if play_mode == 0:
        print('Start Edu!')
        talker('Start edu')

        if language_selection == 0:  # 영어 시작
            print('English start')
            # english_edu()
        else:  # 한글 시작
            print('hangle start')
            hangle_edu()

    # 2 문제모드
    else:
        print('Start Quize!')
        talker('Start quize')

        if language_selection == 0:  # 영어 시작
            print('English start')
            english_quize()
        else:  # 한글 시작
            print('hangle start')
            hangle_quize()


def talker(string):
    time.sleep(2)
    # engine = pyttsx3.init() # tts init
    # engine.setProperty('rate', 100)
    # engine.say(string)
    # engine.runAndWait()


def hangle_edu():
    solenoid = SolenoidController()

    # 버튼 출력(초성)
    for i in range(len(hangle_front)):
        button_up = hangle_front[i]
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

    # 버튼 출력(중성)
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

    # 버튼 출력(종성)
    for i in range(len(hangle_end)):
        button_up = hangle_end[i]
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


def english_quize():
    for i in range(len(english)):
        problem = english[random.randint(1, 26)]  # 문제

        # 스피커 출력
        mock_sound_controller.play_sound()
        time.sleep(2.0)

        answer = input()  # 정답입력 받고

        # if  == :  #정답확인
        #     talker('success')
        #     print('success')
        #
        # else:
        #     talker('fail')
        #     print('fail')


def hangle_quize():
    for i in range(len(english)):
        problem = english[random.randint(1, 26)]  # 문제
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


from mock_braille_controller import ButtonListener
import enum


class Language(enum.Enum):
    KOREA = 0
    ENGLISH = 1


class GameMode(enum.Enum):
    QUIZ = 0
    EDUCATION = 1


class TeachingMachine:
    Language = Language.KOREA
    GameMode = GameMode.EDUCATION
    buttonListener = ButtonListener()
    solenoid = SolenoidController()
    edu_index = 0

    def __init__(self):
        self.buttonListener.set_on_click_lang_change_btn(self.on_click_lang_change)
        self.buttonListener.set_on_click_mode_change_btn(self.on_click_mode_change)
        self.buttonListener.set_on_click_next_btn(self.on_click_next)
        self.buttonListener.set_on_click_pre_btn(self.on_click_pre)

    def process(self):
        print("prcesss")
        self.english_edu()

    def on_click_lang_change(self):
        if self.Language == Language.KOREA:
            self.Language = Language.ENGLISH
        else:
            self.Language = Language.KOREA

    def on_click_mode_change(self):
        if self.GameMode == GameMode.EDUCATION:
            self.GameMode = GameMode.QUIZ
        else:
            self.GameMode = GameMode.EDUCATION

    def on_click_next(self):
        self.edu_index += 1
        self.educate()

    def on_click_pre(self):
        self.edu_index -= 1
        self.educate()

    def educate(self):
        if self.edu_index < len(english):
            self.english_edu()
        else:
            self.edu_index = 0
        self.english_edu()

    def english_edu(self):
        self.solenoid.offAll()
        braille = english[self.edu_index]
        # 점자 출력
        for j in range(1, len(braille)):
            self.solenoid.on(braille[j])

        # 스피커 출력
        mock_sound_controller.play_sound("영어/" + braille[0] + ".wav")


teachingMachine = TeachingMachine()
teachingMachine.process()
