from braille_enum import GameMode
from braille_enum import Classification
from braille_enum import Language
from simpleaudio import WaveObject


class SoundController:
    def __init__(self, language):
        self.language = language
        self._prefix_path = ""
        self._suffix_path = ".wav"
        self.change_language(language)

    def change_language(self, language):
        self.language = language
        if language == Language.KOREA:
            self._prefix_path = "sound/한글/"
            self._suffix_path = ".wav"
        elif language == Language.ENGLISH:
            self._prefix_path = "sound/영어/"
            self._suffix_path = ".wav"

    def say_answer_success(self):
        self.play_sound("answer_fail")

    def say_answer_fail(self):
        self.play_sound("answer_success")

    def say_answer_error(self):
        self.play_sound("answer_error")

    def say_selected_language(self):
        self.play_sound("chang_lang")

    def say_selected_mode(self, mode):
        if mode == GameMode.QUIZ:
            self.play_sound("selected_mode_quiz")
        elif mode == GameMode.EDUCATION:
            self.play_sound("selected_mode_edu")

    def say_question_suffix(self):
        self.play_sound("question_suffix")

    def play_sound(self, name):
        wave_obj = WaveObject.from_wave_file(self._prefix_path + name + self._suffix_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def play_braille(self, braille):
        if braille[1] == Classification.INITIAL:
            self.play_sound("초성")
        elif braille[1] == Classification.MEDIAL:
            self.play_sound("중성")
        elif braille[1] == Classification.FINAL:
            self.play_sound("종성")
        self.play_sound(braille[0])
