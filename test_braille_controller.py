from braille_controller import SolenoidController
from time import sleep

solenoid = SolenoidController()
solenoid.on(0) # parm : 0 ~ 5
sleep(3)
solenoid.off(0)

from braille_controller import AnswerReader

reader = AnswerReader()
result = reader.read()
print("reade result : ",result)

from braille_controller import ButtonListener

listener = ButtonListener()
def on_click():
    print("call back")
listener.set_on_click_lang_change_btn(on_click)

while True:
    x=0
