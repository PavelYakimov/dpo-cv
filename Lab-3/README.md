# Лабораторная работа 3. Работа с веб-камерой

## Цель

Отработать навыки работы с веб-камерой с использованием OpenCV.

## Задачи

1. Считать видеопоток с веб-камеры, реализовать отображение видеопотока в блокноте.
2. Детектировать лица на кадрах видеопотока с использованием метода cv2.CascadeClassifier.
3. Экстрактировать признаки из изображения детектированного лица.
4. Создать набор данных (признаков) своего лица.
5. Реализовать метод сравнения признаков лица, детектируемого в потоке, с набором признаков из п.4. В случае нахождения "похожего" лица в наборе данных признать лицо в видеопотоке идентифицированным (eg. "Павел Якимов"), иначе: "Unknown person".
6. Вывести результат идентификации на экран
