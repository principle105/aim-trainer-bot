import cv2, time, numpy
from pynput.keyboard import Listener
from mss import mss
from pymouse import PyMouse

m = PyMouse()
box = {"left": 0, "top": 270, "width": 1439, "height": 452}


def take_screenshot():
    with mss() as sct:
        return numpy.array(sct.grab(box))


def check_screen():
    screen = take_screenshot()
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    for y in range(0, len(screen), 30):
        for x in range(0, len(screen[y]), 30):
            if screen[y][x] == 189:
                m.click((x / 2 + box["left"]), (y / 2 + box["top"]))
                return


def on_press(key):
    if str(key) == "'|'":
        for _ in range(31):
            check_screen()
            time.sleep(0.02)


if __name__ == "__main__":
    with Listener(on_press=on_press) as listener:
        listener.join()
