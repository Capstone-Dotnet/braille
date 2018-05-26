import enum


class Language(enum.Enum):
    KOREA = 0
    ENGLISH = 1


class GameMode(enum.Enum):
    QUIZ = 0
    EDUCATION = 1


class Classification(enum.Enum):
    INITIAL = 0
    MEDIAL = 1
    FINAL = 2
    ABBREVIATION = 3
    ALPHABET = 4
