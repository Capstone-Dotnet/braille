# -*- coding: utf-8 -*-
from braille_dictionary import BrailleDictionary
from braille_enum import GameMode
from braille_enum import Language
from mock_braille_controller import AnswerReader
from mock_braille_controller import ButtonListener
from mock_braille_controller import SolenoidController
from mock_sound_controller import SoundController


class TeachingMachine:
    Language = Language.KOREA
    GameMode = GameMode.EDUCATION
    buttonListener = ButtonListener()
    solenoid = SolenoidController()
    answerReader = AnswerReader()
    dictionary = BrailleDictionary()
    soundController = SoundController(Language)
    edu_index = 0
    problem = []

    def __init__(self):
        self.buttonListener.set_on_click_lang_change_btn(self.on_click_lang_change)
        self.buttonListener.set_on_click_mode_change_btn(self.on_click_mode_change)
        self.buttonListener.set_on_click_next_btn(self.on_click_next)
        self.buttonListener.set_on_click_pre_btn(self.on_click_pre)
        self.buttonListener.set_on_click_submit_answer_btn(self.on_click_submit_answer)

    def process(self):
        print("prcesss")
        self.educate()

    def on_click_submit_answer(self):
        answer = self.answerReader.read_and_get_abbreviation()

        fail_flag = 0
        if len(self.problem) == len(answer):
            for i in range(len(answer)):
                if self.problem[i] != answer[i]:
                    fail_flag += 1
        else:
            fail_flag += 1

        if fail_flag == 0:
            self.soundController.say_answer_success()
            self.english_quiz()
        else:
            self.soundController.say_answer_fail()

    def on_click_lang_change(self):
        if self.Language == Language.KOREA:
            self.Language = Language.ENGLISH
            self.soundController.change_language(Language.ENGLISH)
        else:
            self.Language = Language.KOREA
            self.soundController.change_language(Language.KOREA)
        self.edu_index = 0
        self.soundController.say_selected_language()

    def on_click_mode_change(self):
        if self.GameMode == GameMode.EDUCATION:
            self.GameMode = GameMode.QUIZ
        else:
            self.GameMode = GameMode.EDUCATION
        self.soundController.say_selected_mode(self.GameMode)

    def on_click_next(self):
        braille = self.dictionary.next_word()
        self.educate(braille)

    def on_click_pre(self):
        braille = self.dictionary.pre_word()
        self.educate(braille)

    def educate(self, braille):
        self.solenoid.offAll()
        # 점자 출력
        for j in range(1, len(braille)):
            self.solenoid.on(braille[j])

        self.soundController.play_sound("sound/" + braille[0] + ".wav")

    def english_quiz(self):
        braille = self.dictionary.random_word()
        self.soundController.play_sound("sound/" + braille + ".wav")


teachingMachine = TeachingMachine()
teachingMachine.process()
