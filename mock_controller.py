
class SolenoidController:
    def on(self,braille_num): # braille_num = 0 ~ 5
        print("solenoid on : ",braille_num)

    def off(self,braille_num):
        print("solenoid off : ",braille_num)

class AnswerReader:
    def read(self):
        result=[False,False,False,False,False,False]
        return result #return [True or False, ... , True or False]

class ButtonListener:

    def set_on_click_lang_change_btn(self, on_click):
        print("set call back function:",on_click)
    
    def set_on_click_next_btn(self, on_click):
        print("set call back function:",on_click)

    def set_on_click_pre_btn(self, on_click):
        print("set call back function:",on_click)

    def set_on_click_mode_change_btn(self,on_click):
        print("set call back function:",on_click)

    def set_on_click_submit_answer_btn(self,on_click):
        print("set call back function:",on_click)


