# Задание на лабораторную работу 2: OpenCV. Basic operations

Цель: овладеть навыками работы с изображениями с использованием OpenCV

Для выполнения лабораторной работы будет полезно пользоваться [блокнотом](https://github.com/PavelYakimov/dpo-cv/blob/main/28-09-2021/OpenCV.ipynb), который был создан в ходе мастер-класса 28.09.2021, и материалами [документации OpenCV](https://docs.opencv.org/master/d7/d16/tutorial_py_table_of_contents_core.html)

Задачи:
1) Считать изображение с диска. Вывести изображение из переменной на экран.
Использовать для этого методы cv2.imread() и cv2.imshow(). Следует помнить, что imshow в блокнотах Jupyter не работает, поэтому нужно пользоваться либо библиотекой [Matplotlib](https://www.pyimagesearch.com/2014/11/03/display-matplotlib-rgb-image/), либо [патчем](https://coderoad.ru/57090598/%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-cv2-imshow-%D0%B2-google-Colab) от Google, если работа выполняется в Google Colab.

2) Получить несколько видов бинарных изображений при помощи метода [cv2.threshold()](https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57).
Использовать при этом следует различные типы операций, которые описаны [здесь](https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#gaa9e58d2860d4afa658ef70a9b1115576).
Вывести на экран и сравнить изображения.

3) Перевести оригинальное изображение в цветовое пространство HSV. Вывести на экран по отдельности каналы H, S и V.
