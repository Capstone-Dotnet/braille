from braille_controller import SolenoidController
from time import sleep

solenoid = SolenoidController()
def on_all():
    solenoid.on(0) # parm : 0 ~ 5
    sleep(1)
    solenoid.on(1)
    sleep(1)
    solenoid.on(2)
    sleep(1)
    solenoid.on(3)
    sleep(1)
    solenoid.on(4)
#   sleep(1)
#    solenoid.on(5)
def off_all():
    sleep(1)
    solenoid.off(0) # parm : 0 ~ 5
    sleep(1)
    solenoid.off(1)
    sleep(1)
    solenoid.off(2)
    sleep(1)
    solenoid.off(3)
    sleep(1)
    solenoid.off(4)
 #   sleep(1)
#    solenoid.off(5)

#solenoid.on(0)
#solenoid.on(5)
#sleep(100)
on_all()
sleep(1)
off_all()
sleep(1)
solenoid.on(0) # parm : 0 ~ 5
solenoid.on(1)
solenoid.on(2)
solenoid.on(3)
solenoid.on(4)
solenoid.on(5)
sleep(2)#
