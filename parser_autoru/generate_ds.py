import os
import random

from PIL import Image


def process_folder(folder_path):
    # Получаем список файлов и папок в текущей папке
    items = os.listdir(folder_path)

    subfolders = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]
    if not subfolders and len(items) < 50:
        difference = 50 - len(items)
        print(f"В папке {folder_path} меньше 50 элементов. Разница: {difference}")

        # Генерируем изображения на основе тех, которые уже есть в папке
        for i in range(difference):
            img_path_old = os.path.join(folder_path, f"img_{i+1}.png")
            img_path = os.path.join(folder_path, f"img_{len(items) + i}.png")
            last_image = Image.open(img_path_old)
            img = last_image.rotate(180*random.random())
            img.save(img_path)
            print(f"Создано изображение: {img_path}")

    for item in subfolders:
        process_folder(os.path.join(folder_path, item))

    for item in [item for item in items if not os.path.isdir(os.path.join(folder_path, item))]:
        print(f"Обрабатываем файл: {os.path.join(folder_path, item)}")


root_folder = "C:\\Users\\Александр\\PycharmProjects\\autorepairai_2\\parser_autoru\\new"
process_folder(root_folder)
