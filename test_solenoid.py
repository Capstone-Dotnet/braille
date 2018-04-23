from braille_controller import SolenoidController
from time import sleep

solenoid = SolenoidController()
solenoid.on(0) # parm : 0 ~ 5
solenoid.on(1)
solenoid.on(2)
solenoid.on(3)
solenoid.on(4)
solenoid.on(5)
sleep(60)

