import os

os.system("pip install numpy")
os.system("pip install opencv-python")

import cv2
import numpy as np

def create_timecode_video(fps):
    # Создаем пустое видео с заданными параметрами
    width, height = 640, 480
    video = cv2.VideoWriter('timecode.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

    # Задаем начальное время в виде hh:mm:ss
    # print("hh:mm:ss")
    time = "00:00:00"
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Инициализируем переменные для цветовой схемы в видео хлопушки (чб)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Переменные для позиции и размера текста
    text_offset_x = 20
    text_offset_y = int(height/2)
    text_thickness = 2
    text_scale = 2

    # Создаем бесконечный цикл для создания каждого кадра
    while True:
        # Создаем черный фон для текущего кадра
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Добавляем текст с текущим временем на черный фон
        cv2.putText(frame, time, (text_offset_x, text_offset_y), font, text_scale, white, text_thickness, cv2.LINE_AA)

        # Записываем текущий кадр в видео
        video.write(frame)

        # Увеличиваем время на 1 кадр
        time = increase_time(time, fps)

        # Для остановки программы после записи 5 секунд видео       
        if time == "00:00:05":
            break

    # Освобождаем видео и закрываем окна
    video.release()
    cv2.destroyAllWindows()

def increase_time(time, fps):
    # Преобразуем строку времени в секунды
    hours, minutes, seconds = map(int, time.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Увеличиваем на 1 секунду в зависимости от частоты кадров
    total_seconds += 1 / fps

    # Преобразуем обратно в строку времени (hh:mm:ss)
    hours = int(total_seconds / 3600)
    minutes = int((total_seconds % 3600) / 60)
    seconds = int(total_seconds % 60)
    time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return time

# Задаем частоты кадров для создания видео
fps_list = [24, 30, 25, 50, 60, 120]

# Создаем видео с таймкодами для каждой частоты кадров
for fps in fps_list:
    create_timecode_video(fps)

# softy_plug