from gpiozero import Button
from gpiozero import OutputDevice


class SolenoidController:
    SOLENOID = []

    def __init__(self):
        SOLENOID_PIN = [13, 19, 26, 16, 20, 21]
        for i in SOLENOID_PIN:
            self.SOLENOID.append(OutputDevice(i))
        # for i in range(2, 6):
        #     self.SOLENOID[i].on()
        self.off_all()

    def __del__(self):
        for i in self.SOLENOID:
            i.close()

    def on(self, braille_num):  # braille_num = 0 ~ 5
        # if braille_num < 2:
        self.SOLENOID[braille_num].on()
        # else:
        #     self.SOLENOID[braille_num].off()

    def off(self, braille_num):
        # if braille_num < 2:
        self.SOLENOID[braille_num].off()
        # else:
        #     self.SOLENOID[braille_num].on()

    def off_all(self):
        for i in range(6):
            self.SOLENOID[i].off()

        print("solenoid offAll ")


class AnswerReader:
    ANSWER_BTN = []

    def __init__(self):
        ANSWER_PIN = [17, 18, 27, 23, 22, 24]
        for i in ANSWER_PIN:
            self.ANSWER_BTN.append(Button(i))

    def __del__(self):
        for i in self.ANSWER_BTN:
            i.close()

    def read(self):
        result = []
        for i in range(6):
            result.append(self.ANSWER_BTN[i].is_pressed)
        return result  # return [True or False, ... , True or False]

    def read_and_get_abbreviation(self):
        answer = []
        for i in range(6):
            if self.ANSWER_BTN[i].is_pressed:
                answer.append(i)
        return answer


class ButtonListener:
    LANGUAGE_CHANGE_BTN = Button(9)
    NEXT_BTN = Button(8)
    PRE_BTN = Button(7)
    MODE_CHANGE_BTN = Button(11)
    SUBMIT_ANSWER_BTN = Button(25)

    def __del__(self):
        self.LANGUAGE_CHANGE_BTN.close()
        self.NEXT_BTN.close()
        self.PRE_BTN.close()
        self.MODE_CHANGE_BTN.close()
        self.SUBMIT_ANSWER_BTN.close()

    def set_on_click_lang_change_btn(self, on_click):
        print("set_on_click_lang_change_btn")
        self.LANGUAGE_CHANGE_BTN.when_pressed = on_click

    def set_on_click_next_btn(self, on_click):
        print("set_on_click_next_btn")
        self.NEXT_BTN.when_pressed = on_click

    def set_on_click_pre_btn(self, on_click):
        print("set_on_click_pre_btn")
        self.PRE_BTN.when_pressed = on_click

    def set_on_click_mode_change_btn(self, on_click):
        print("set_on_click_mode_change_btn")
        self.MODE_CHANGE_BTN.when_pressed = on_click

    def set_on_click_submit_answer_btn(self, on_click):
        print("set_on_click_submit_answer_btn")
        self.SUBMIT_ANSWER_BTN.when_pressed = on_click
