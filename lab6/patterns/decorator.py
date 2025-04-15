from typing import Callable
from functools import reduce


Color = tuple[int, int, int]


def brighter(color: Color) -> Color:
    return tuple(min(int(c * 1.1), 255) for c in color)

def darker(color: Color) -> Color:
    return tuple(max(int(c * 0.9), 0) for c in color)

class Camera:
    def __init__(self, *filters: Callable[[Color], Color]):
        
        self.filter = reduce(lambda f, g: lambda x: g(f(x)), filters, lambda x: x)

    def snap(self, input_color: Color) -> Color:
        return self.filter(input_color)

def print_camera(camera: Camera):
    input_color = (125, 125, 125)
    print(camera.snap(input_color))

def main():
    print_camera(Camera())                            
    print_camera(Camera(brighter))                     
    print_camera(Camera(darker))                       
    print_camera(Camera(darker, brighter))             

if __name__ == "__main__":
    main()
