import pyautogui
from time import sleep
from PIL import ImageGrab, ImageOps

replay = (962, 292)
dino = (661, 293, 703, 338)
delta = 85
delta2 = 15


def imagegrab():
    bbox = (dino[0] + delta, dino[1], dino[2] + delta, dino[3] - delta2)
    img = ImageGrab.grab(bbox)
    grayimg = ImageOps.grayscale(img)
    # grayimg.save("target.jpg")
    # b = grayimg.getcolors()
    a = sum(map(sum, grayimg.getcolors()))
    return a


def jump():
    pyautogui.keyDown('space')
    sleep(0.001)
    pyautogui.keyUp('space')
    sleep(0.001)


def restart():
    pyautogui.click(replay)


def main():
    restart()
    while True:
        imagegrab()
        if (imagegrab() != 1507):
            jump()


if __name__ == "__main__":
    main()