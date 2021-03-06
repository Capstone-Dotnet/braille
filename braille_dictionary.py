from braille_enum import Classification
from braille_enum import Language
import random


class BrailleDictionary:
    _english = [["a", Classification.ALPHABET, 0], ["b", Classification.ALPHABET, 0, 2],
                ["c", Classification.ALPHABET, 0, 1], ["d", Classification.ALPHABET, 0, 1, 3],
                ["e", Classification.ALPHABET, 0, 3], ["f", Classification.ALPHABET, 0, 1, 2],
                ["g", Classification.ALPHABET, 0, 1, 2, 3], ["h", Classification.ALPHABET, 0, 2, 3],
                ["i", Classification.ALPHABET, 1, 2],
                ["j", Classification.ALPHABET, 1, 2, 3], ["k", Classification.ALPHABET, 0, 4],
                ["l", Classification.ALPHABET, 0, 2, 4], ["m", Classification.ALPHABET, 0, 1, 4],
                ["n", Classification.ALPHABET, 0, 1, 3, 4], ["o", Classification.ALPHABET, 0, 3, 4],
                ["p", Classification.ALPHABET, 0, 1, 2, 4],
                ["q", Classification.ALPHABET, 0, 1, 2, 3, 4], ["r", Classification.ALPHABET, 0, 2, 3, 4],
                ["s", Classification.ALPHABET, 1, 2, 4], ["t", Classification.ALPHABET, 1, 2, 3, 4],
                ["u", Classification.ALPHABET, 0, 4, 5],
                ["v", Classification.ALPHABET, 0, 2, 4, 5], ["w", Classification.ALPHABET, 1, 2, 3, 5],
                ["x", Classification.ALPHABET, 0, 1, 4, 5], ["y", Classification.ALPHABET, 0, 1, 3, 4, 5],
                ["z", Classification.ALPHABET, 0, 3, 4, 5]]
    _korea = [["ㄱ", Classification.INITIAL, 1], ["ㄴ", Classification.INITIAL, 0, 1],
              ["ㄷ", Classification.INITIAL, 1, 2], ["ㄹ", Classification.INITIAL, 3],
              ["ㅁ", Classification.INITIAL, 0, 3], ["ㅂ", Classification.INITIAL, 1, 3],
              ["ㅅ", Classification.INITIAL, 5], # ["ㅇ", Classification.INITIAL, 0, 1, 2, 3] 초성 'ㅇ' 제외, 'ㅇ'이 모음앞에 쓰일 때는 생략, 'ㅇ'만 적을때는 앞에 1~6점을 다 적어야함
              ["ㅈ", Classification.INITIAL, 1, 5], ["ㅊ", Classification.INITIAL, 3, 5],
              ["ㅋ", Classification.INITIAL, 0, 1, 2], ["ㅌ", Classification.INITIAL, 0, 2, 3],
              ["ㅍ", Classification.INITIAL, 0, 1, 3], ["ㅎ", Classification.INITIAL, 1, 2, 3],
              ["ㅏ", Classification.MEDIAL, 0, 2, 5], ["ㅑ", Classification.MEDIAL, 1, 3, 4],
              ["ㅓ", Classification.MEDIAL, 1, 2, 4], ["ㅕ", Classification.MEDIAL, 0, 3, 5],
              ["ㅗ", Classification.MEDIAL, 0, 4, 5], ["ㅛ", Classification.MEDIAL, 1, 4, 5],
              ["ㅜ", Classification.MEDIAL, 0, 1, 4], ["ㅠ", Classification.MEDIAL, 0, 1, 5],
              ["ㅡ", Classification.MEDIAL, 1, 2, 5], ["ㅣ", Classification.MEDIAL, 0, 3, 4],
              ["ㅐ", Classification.MEDIAL, 0, 2, 3, 4], ["ㅔ", Classification.MEDIAL, 0, 1, 3, 4],
              ["ㄱ", Classification.FINAL, 0],
              ["ㄴ", Classification.FINAL, 2, 3], ["ㄷ", Classification.FINAL, 3, 4],
              ["ㄹ", Classification.FINAL, 2], ["ㅁ", Classification.FINAL, 2, 5], ["ㅂ", Classification.FINAL, 0, 2],
              ["ㅅ", Classification.FINAL, 4], ["ㅇ", Classification.FINAL, 2, 3, 4, 5],
              ["ㅈ", Classification.FINAL, 0, 4], ["ㅊ", Classification.FINAL, 2, 4],
              ["ㅋ", Classification.FINAL, 2, 3, 4], ["ㅌ", Classification.FINAL, 2, 4, 5],
              ["ㅍ", Classification.FINAL, 2, 3, 5], ["ㅎ", Classification.FINAL, 3, 4, 5]]

    def __init__(self):
        self._current_dic_lng = self._korea
        self._current_page = 0

    def next_word(self):
        self._current_page += 1
        if self._current_page >= len(self._current_dic_lng):
            self._current_page = 0
        return self._current_dic_lng[self._current_page]

    def pre_word(self):
        self._current_page -= 1
        if self._current_page < 0:
            self._current_page = len(self._current_dic_lng) - 1
        return self._current_dic_lng[self._current_page]

    def random_word(self):
        return self._current_dic_lng[random.randint(0, len(self._current_dic_lng) - 1)]

    def change_language(self, language):
        if language == Language.KOREA:
            self._current_dic_lng = self._korea
        elif language == Language.ENGLISH:
            self._current_dic_lng = self._english
        self._current_page = 0
