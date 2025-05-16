from random import randint

from pygame import mixer

from src.resource_path import get_resource_path

BASE_PATH = 'sound/'


def play_chips_sound() -> None:
    which = randint(1, 3)
    sound = f"chips_{which}.mp3"
    play_sound(sound)


def play_deal_sound() -> None:
    which = randint(1, 4)
    sound = f"deal_{which}.mp3"
    play_sound(sound)


def play_shuffle_sound() -> None:
    sound = "shuffle.mp3"
    play_sound(sound)


def play_sound(sound: str) -> None:
    mixer.init()
    path = get_resource_path(BASE_PATH + sound)
    mixer.music.load(path)
    mixer.music.play()
