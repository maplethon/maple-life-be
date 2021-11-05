from enum import Enum, auto


class IconTypes(Enum):
    sun = auto()
    droplet = auto()
    music = auto()


print(IconTypes["sun"].name)
