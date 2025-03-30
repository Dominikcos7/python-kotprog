from random import randint

from pygame import mixer

BASE_PATH = './src/sound/'


def play_sound(sound: str) -> None:
    mixer.init()
    mixer.music.load(BASE_PATH + sound)
    mixer.music.play()


def play_chips_sound() -> None:
    which = randint(1, 3)
    sound = f"chips_{which}.mp3"
    play_sound(sound)
