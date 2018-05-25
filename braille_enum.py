import enum


class Language(enum.Enum):
    KOREA = 0
    ENGLISH = 1


class GameMode(enum.Enum):
    QUIZ = 0
    EDUCATION = 1


class Classification(enum.Enum):
    INITIAL = enum.auto()
    MEDIAL = enum.auto()
    FINAL = enum.auto()
    ABBREVIATION = enum.auto()
    ALPHABET = enum.auto()
