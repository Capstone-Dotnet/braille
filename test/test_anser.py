from braille_controller import SolenoidController
from time import sleep
from braille_controller import AnswerReader
solenoid = SolenoidController()

reader = AnswerReader()
while True:
    result = reader.read()
    print("reade result : ",result)
    for i in range(6):
        if result[i] == True:
            solenoid.on(i)
        else:
            solenoid.off(i)
    #    sleep(1)
