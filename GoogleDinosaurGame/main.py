import pyautogui
from PIL import Image,ImageGrab
import time


def click(key):
    pyautogui.keyDown(key)
    time.sleep(0.05)  # Short press duration
    pyautogui.keyUp(key)  # Release the key


def isCollision(data):
    # Check collision for birds (upper area)
    for x in range(530, 560):  # Horizontal range
        for y in range(80, 127):  # Vertical range
            if data[x, y] < 100:  # Darker pixel threshold
                click("down")
                return True

    # Check collision for cactus (lower area)
    for x in range(530, 620):  # Horizontal range
        for y in range(130, 160):  # Vertical range
            if data[x, y] < 100:  # Darker pixel threshold
                click("up")
                return True
    return False


def debug_visualization(image):
    # Visual feedback for detection areas
    data = image.load()

    # Mark bird detection area
    for x in range(530, 560):
        for y in range(80, 127):
            data[x, y] = 100  # Gray out bird zone

    # Mark cactus detection area
    for x in range(127, 190):
        for y in range(160, 165):
            data[x, y] = 200  # Gray out cactus zone

    image.show()


if __name__ == "__main__":
    time.sleep(3)
    print("Starting detection...")

    while True:
        # Capture screen (convert to grayscale)
        image = ImageGrab.grab().convert('L')
        data = image.load()
        image.save("reference.png")

        if isCollision(data):
            print("Action triggered!")

        # Uncomment for debugging visualization
        # debug_visualization(image.copy())

        time.sleep(0.05)  # Reduce CPU usage