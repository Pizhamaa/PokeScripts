import random as rm
import keyboard
import time as tm
import pyautogui



areas = [
    (331, 911, 508, 960), # 1 атака
    (528, 911, 706, 960), # 2 атака
    (725, 911, 903, 960), # 3 атака
    (921, 911, 1098, 960) # 4 атака
]

running = False
paused = False
click_counter = 0

print('F6 — старт')
print('F8 — пауза/продолжить')
print('ESC — выход')

def start():
    global running
    running = True
    print('Запущено')

def pause():
    global paused
    paused = not paused
    print('Пауза' if paused else 'Продолжено')

keyboard.add_hotkey('f6', start)
keyboard.add_hotkey('f8', pause)

def human_move_and_click(x, y):
    if rm.random()  < 0.3:
        for _ in range(rm.randint(1, 3)):
            dx = rm.randint(-5, 5)
            dy = rm.randint(-5, 5)
            pyautogui.moveRel(dx, dy, duration=rm.uniform(0.05, 0.12))

    duration = rm.uniform(0.15, 0.35)
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)

    tm.sleep(rm.uniform(0.05, 0.15))

    pyautogui.click()

while True:
    if keyboard.is_pressed('esc'):
        print('Остановлено')
        break

    if running and not paused:
        for x_min, y_min, x_max, y_max in areas:

            if keyboard.is_pressed('esc'):
                print('Остановлено')
                exit()

            while paused:
                tm.sleep(0.1)

            x = rm.randint(x_min, x_max)
            y = rm.randint(y_min, y_max)

            human_move_and_click(x, y)

            click_counter += 1

            delay = rm.uniform(1, 3)

            if rm.randint(1, 40) == 1:
                long_pause = rm.uniform(4, 8)
                print(f'Делаем длинную {long_pause:.2f} сек')
                delay += long_pause

            tm.sleep(delay)

    else:
        tm.sleep(0.1)
















