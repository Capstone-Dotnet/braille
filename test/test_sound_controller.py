import sound_controller
import time

sound_controller.play_sound("sounds/test_sound.wav")
time.sleep(2)

from mock import mock_sound_controller

mock_sound_controller.play_sound("sounds/test_sound.wav")


