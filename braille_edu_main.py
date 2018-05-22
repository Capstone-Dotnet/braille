# -*- coding: utf-8 -*-
from mock_braille_controller import SolenoidController
from mock_braille_controller import ButtonListener
from mock_braille_controller import AnswerReader
import mock_sound_controller
import random
import enum

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
    answerReader = AnswerReader()
    edu_index = 0

    def __init__(self):
        self.buttonListener.set_on_click_lang_change_btn(self.on_click_lang_change)
        self.buttonListener.set_on_click_mode_change_btn(self.on_click_mode_change)
        self.buttonListener.set_on_click_next_btn(self.on_click_next)
        self.buttonListener.set_on_click_pre_btn(self.on_click_pre)
        self.buttonListener.set_on_click_submit_answer_btn(self.on_click_submit_answer)

    def process(self):
        print("prcesss")
        self.english_edu()

    def on_click_submit_answer(self):
        temp = self.answerReader.read()
        answer = []
        for i in range(6):
            if temp[i]:
                answer.append(i)

        fail_flag = 0
        if len(self.problem) == len(answer):
            for i in range(len(answer)):
                if self.problem[i] != answer[i]:
                    fail_flag += 1
        else:
            fail_flag += 1

        if fail_flag == 0:
            print('success')
            self.english_quiz()
        else:
            print('fail')

    def on_click_lang_change(self):
        if self.Language == Language.KOREA:
            self.Language = Language.ENGLISH
        else:
            self.Language = Language.KOREA
        self.edu_index = 0

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

    def english_quiz(self):
        self.problem = english[random.randint(1, 26)]  # 문제
        # 스피커 출력
        mock_sound_controller.play_sound("sound/" + self.problem[0] + ".wav")


teachingMachine = TeachingMachine()
teachingMachine.process()
