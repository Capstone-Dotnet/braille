from gpiozero import Button
from gpiozero import OutputDevice

class SolenoidController:
    SOLENOID=[]
    def __init__(self):
        """
        SOLENOID_0=13  SOLENOID_1=16
        SOLENOID_2=19  SOLENOID_3=20
        SOLENOID_4=26  SOLENOID_5=21
        """
        SOLENOID_PIN=[13,16,19,20,26,21]
        for i in SOLENOID_PIN:
            self.SOLENOID.append(OutputDevice(i))

    def __del__(self):
        for i in self.SOLENOID:
            i.close()

    def on(self,braille_num): # braille_num = 0 ~ 5
        self.SOLENOID[braille_num].on()

    def off(self,braille_num):
        self.SOLENOID[braille_num].off()

class AnswerReader:
    ANSWER_BTN=[]
    def __init__(self):
        ANSWER_PIN=[17,18,27,23,22,24]
        for i in ANSWER_PIN:
            self.ANSWER_BTN.append(Button(i))
    
    def __del__(self):
        for i in self.ANSWER_BTN:
            i.close()
    
    def read(self):
        result = []
        for i in range(6):
            result.append(self.ANSWER_BTN[i].is_pressed)
        return result #return [True or False, ... , True or False]

class ButtonListener:
    LANGUAGE_CHANGE_BTN=Button(9)
    NEXT_BTN=Button(8)
    PRE_BTN=Button(7)
    MODE_CHANGE_BTN=Button(11)
    SUBMIT_ANSWER_BTN=Button(25)

    def __del__(self):
        self.LANGUAGE_CHANGE_BTN.close()
        self.NEXT_BTN.close()
        self.PRE_BTN.close()
        self.MODE_CHANGE_BTN.close()
        self.SUBMIT_ANSWER_BTN.close()

    def set_on_click_lang_change_btn(self, on_click):
        self.LANGUAGE_CHANGE_BTN.when_pressed=on_click
    
    def set_on_click_next_btn(self, on_click):
        self.NEXT_BTN.when_pressed=on_click
    
    def set_on_click_pre_btn(self, on_click):
        self.PRE_BTN.when_pressed=on_click

    def set_on_click_mode_change_btn(self,on_click):
        self.MODE_CHANGE_BTN.when_pressed=on_click

    def set_on_click_submit_answer_btn(self,on_click):
        self.SUBMIT_ANSWER_BTN.when_pressed=on_click

