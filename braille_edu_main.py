# -*- coding: utf-8 -*-
from braille_dictionary import BrailleDictionary
from braille_enum import GameMode
from braille_enum import Language
from mock_braille_controller import AnswerReader
from mock_braille_controller import ButtonListener
from mock_braille_controller import SolenoidController
from mock_sound_controller import SoundController


class TeachingMachine:

    def __init__(self):
        self._buttonListener = ButtonListener()
        self._solenoid = SolenoidController()
        self._answerReader = AnswerReader()
        self._language = Language.KOREA
        self._dictionary = BrailleDictionary(self._language)
        self._soundController = SoundController(self._language)

        self._buttonListener.set_on_click_lang_change_btn(self.on_click_lang_change)
        self._buttonListener.set_on_click_mode_change_btn(self.on_click_mode_change)
        self._buttonListener.set_on_click_next_btn(self.on_click_next)
        self._buttonListener.set_on_click_pre_btn(self.on_click_pre)
        self._buttonListener.set_on_click_submit_answer_btn(self.on_click_submit_answer)

        self._game_mode = GameMode.EDUCATION
        self.problem = []

    def process(self):
        print("prcesss")
        self.on_click_next()

    def on_click_submit_answer(self):
        answer = self._answerReader.read_and_get_abbreviation()

        fail_flag = 0
        if len(self.problem) == len(answer):
            for i in range(len(answer)):
                if self.problem[i] != answer[i]:
                    fail_flag += 1
        else:
            fail_flag += 1

        if fail_flag == 0:
            self._soundController.say_answer_success()
            self.english_quiz()
        else:
            self._soundController.say_answer_fail()

    def on_click_lang_change(self):
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
        if self._game_mode == GameMode.EDUCATION:
            self._game_mode = GameMode.QUIZ
        else:
            self._game_mode = GameMode.EDUCATION
        self._soundController.say_selected_mode(self._game_mode)

    def on_click_next(self):
        braille = self._dictionary.next_word()
        self.educate(braille)

    def on_click_pre(self):
        braille = self._dictionary.pre_word()
        self.educate(braille)

    def educate(self, braille):
        self._solenoid.off_all()
        # 점자 출력
        for j in range(1, len(braille)):
            self._solenoid.on(braille[j])

        self._soundController.play_sound("sound/" + braille[0] + ".wav")

    def english_quiz(self):
        braille = self._dictionary.random_word()
        self._soundController.play_sound("sound/" + braille + ".wav")


teachingMachine = TeachingMachine()
teachingMachine.process()
