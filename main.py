import pyautogui, keyboard
from os import system

system(f"title Color Picker by Klaro")


class Base:
    running = True


def stop() -> Base.running:
    Base.running = False


keyboard.add_hotkey('ctrl+c', stop)


def main():
    while Base.running:
        x, y = pyautogui.position()
        rgb = pyautogui.pixel(x, y)
        rgbToHex = '#%02x%02x%02x' % rgb
        print(f"\033[38;5;82mPosition\033[0m: \033[38;5;226mX\033[0m: \033[38;5;14m{x}\033[0m, \033[38;5;226mY\033[0m: \033[38;5;14m{y}\033[0m \033[38;5;200mRGB\033[0m: {rgb} \033[38;5;208mHEX\033[0m: {rgbToHex} \033[38;5;57mANSI\033[0m: \{'033'}[38;2;{str(rgb[0])};{str(rgb[1])};{str(rgb[2])}m \033[38;5;198mColor\033[0m: [\033[38;2;{str(rgb[0])};{str(rgb[1])};{str(rgb[2])}mPreview\033[0m]")

    input()


if __name__ == "__main__":
    main()