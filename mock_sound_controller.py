from braille_enum import GameMode
from braille_enum import Classification


class SoundController:

    def __init__(self, language):
        self.language = language

    def change_language(self, language):
        self.language = language

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
        print("play : ", path)

    def play_braille(self, braille):
        if braille[1] == Classification.INITIAL:
            print("초성")
        elif braille[1] == Classification.MEDIAL:
            print("중성")
        elif braille[1] == Classification.FINAL:
            print("종성")

        print("play", "sound/" + braille[0] + ".wav")
