from braille_enum import GameMode
from braille_enum import Classification
from braille_enum import Language
import pygame


class SoundController:
    def __init__(self, language):
        self.language = language
        self.mixer = pygame.mixer
        self.mixer.init()
        self._prefix_path = "sound/"
        self._suffix_path = ".wav"

    def change_language(self, language):
        self.language = language
        if language == Language.KOREA:
            self._prefix_path = "sound/한글/"
        elif language == Language.ENGLISH:
            self._prefix_path = "sound/영어/"

    def say_answer_success(self):
        self.play_sound("정답입니다.")

    def say_answer_fail(self):
        self.play_sound("오답입니다.")

    def say_selected_language(self):
        self.play_sound("한국어입니다.")

    def say_selected_mode(self, mode):
        if mode == GameMode.QUIZ:
            self.play_sound("퀴즈모드입니다.")
        elif mode == GameMode.EDUCATION:
            self.play_sound("문제모드입니다.")

    def play_sound(self, path):
        self.mixer.Sound(path).play()
        print("play sound : ", path)

    def play_braille(self, braille):
        if braille[1] == Classification.INITIAL:
            print("초성")
        elif braille[1] == Classification.MEDIAL:
            print("중성")
        elif braille[1] == Classification.FINAL:
            print("종성")

        self.play_sound(self._prefix_path + braille[0] + self._suffix_path)
        print("play ", self._prefix_path + braille[0] + self._suffix_path)
