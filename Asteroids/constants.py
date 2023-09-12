WIDTH = 405
HEIGHT = 720
SCALE = 25
FPS = 60
VELOCITY = 2

def collide(obj1, obj2):
    return obj1.mask.overlap(obj2.mask,(obj2.x - obj1.x, obj2.y - obj1.y))