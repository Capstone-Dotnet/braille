from braille_enum import GameMode
from braille_enum import Classification
from braille_enum import Language
import pygame


class SoundController:
    def __init__(self, language):
        self.language = language
        self.mixer = pygame.mixer
        self.mixer.init()
        self._prefix_path = ""
        self._suffix_path = ".wav"
        self.change_language(language)

    def change_language(self, language):
        self.language = language
        if language == Language.KOREA:
            self._prefix_path = "sound/한글/"
        elif language == Language.ENGLISH:
            self._prefix_path = "sound/영어/"

    def say_answer_success(self):
        print("정답입니다.")

    def say_answer_fail(self):
        print("오답입니다.")

    def say_selected_language(self):
        print("한국어입니다.")

    def say_selected_mode(self, mode):
        if mode == GameMode.QUIZ:
            print("퀴즈모드입니다.")
        elif mode == GameMode.EDUCATION:
            print("문제모드입니다.")

    def play_sound(self, name):
        self.mixer.Sound(self._prefix_path + name + self._suffix_path).play()
        print("play sound : ", self._prefix_path + name + self._suffix_path)

    def play_braille(self, braille):
        if braille[1] == Classification.INITIAL:
            print("초성")
        elif braille[1] == Classification.MEDIAL:
            print("중성")
        elif braille[1] == Classification.FINAL:
            print("종성")
        self.play_sound(braille[0])
