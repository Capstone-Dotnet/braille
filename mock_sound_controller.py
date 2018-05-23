from braille_enum import Language
from braille_enum import GameMode


class SoundController:

    def __init__(self, language):
        self.Language = language

    def change_language(self, language):
        self.Language = language

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
        print("play", path)
