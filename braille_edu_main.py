#!/usr/bin/python3
from braille_dictionary import BrailleDictionary
from braille_enum import GameMode
from braille_enum import Language
from braille_controller import AnswerReader
from braille_controller import ButtonListener
from braille_controller import SolenoidController
from sound_controller import SoundController
import time


class TeachingMachine:

    def __init__(self):
        self._buttonListener = ButtonListener()
        self._solenoid = SolenoidController()
        self._answerReader = AnswerReader()
        self._language = Language.KOREA
        self._dictionary = BrailleDictionary()
        self._soundController = SoundController(self._language)

        self._buttonListener.set_on_click_lang_change_btn(self.on_click_lang_change)
        self._buttonListener.set_on_click_mode_change_btn(self.on_click_mode_change)
        self._buttonListener.set_on_click_next_btn(self.on_click_next)
        self._buttonListener.set_on_click_pre_btn(self.on_click_pre)
        self._buttonListener.set_on_click_submit_answer_btn(self.on_click_submit_answer)

        self._game_mode = GameMode.EDUCATION
        self._problem = []

    def process(self):
        self._soundController.play_intro()
        self.on_click_next()

    def on_click_submit_answer(self):
        print("on_click_submit_answer")
        if self._game_mode == GameMode.QUIZ:
            answer = self._answerReader.read_and_get_abbreviation()
            print(answer)
            print(self._problem)
            fail_flag = 0
            if (len(self._problem) - 2) == len(answer):
                for i in range(len(answer)):
                    if self._problem[i + 2] != answer[i]:
                        fail_flag += 1
            else:
                fail_flag += 1

            if fail_flag == 0:
                self._soundController.say_answer_success()
                self.quiz()
            else:
                self._soundController.say_answer_fail()
        else:
            self._soundController.say_answer_error()

    def on_click_lang_change(self):
        print("on_click_lang_change")
        if self._language == Language.KOREA:
            self._language = Language.ENGLISH
            self._dictionary.change_language(Language.ENGLISH)
            self._soundController.change_language(Language.ENGLISH)
        else:
            self._language = Language.KOREA
            self._dictionary.change_language(Language.KOREA)
            self._soundController.change_language(Language.KOREA)
        self._soundController.say_selected_language()

    def on_click_mode_change(self):
        print("on_click_mode_change")
        if self._game_mode == GameMode.EDUCATION:
            self._solenoid.off_all()
            self._game_mode = GameMode.QUIZ
            self._soundController.say_selected_mode(self._game_mode)
            self.quiz()
        else:
            self._game_mode = GameMode.EDUCATION
            self._soundController.say_selected_mode(self._game_mode)
            self.on_click_next()

    def on_click_next(self):
        print("on_click_next")
        if self._game_mode == GameMode.EDUCATION:
            braille = self._dictionary.next_word()
            self.educate(braille)
        elif self._game_mode == GameMode.QUIZ:
            self.quiz()

    def on_click_pre(self):
        print("on_click_pre")
        if self._game_mode == GameMode.EDUCATION:
            braille = self._dictionary.pre_word()
            self.educate(braille)
        elif self._game_mode == GameMode.QUIZ:
            self.quiz()

    def educate(self, braille):
        print("educate braille : ", braille)
        self._solenoid.off_all()
        for j in range(2, len(braille)):
            self._solenoid.on(braille[j])
        self._soundController.play_braille(braille)

    def quiz(self):
        self._soundController.say_question_prefix()
        self._problem = self._dictionary.random_word()
        self._soundController.play_braille(self._problem)
        self._soundController.say_question_suffix()


teachingMachine = TeachingMachine()
teachingMachine.process()

while True:
    time.sleep(10000)
