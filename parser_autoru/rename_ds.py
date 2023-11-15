import os

# Получаем список файлов в папке
files = os.listdir('C:\\Users\\Александр\\PycharmProjects\\autorepairai_2\\parser_autoru\\car_with_model\\Largus')

# Фильтруем только файлы с названием img_n
image_files = [file for file in files if file.startswith('img_')]

# Получаем индексы из названий файлов
indices = [int(file.split('_')[1].replace(".png", '')) for file in image_files]

# Находим последний индекс
last_index = max(indices)

# Перемещаем изображения из другой папки и переименовываем
source_folder = 'C:\\Users\\Александр\\PycharmProjects\\autorepairai_2\\parser_autoru\\car_with_model\\nen'
for i, file in enumerate(os.listdir(source_folder)):
    new_name = f'img_{last_index + i + 1}.png'  # Предполагается, что изображения в формате jpg
    os.rename(os.path.join(source_folder, file), os.path.join('C:\\Users\\Александр\\PycharmProjects\\autorepairai_2\\parser_autoru\\car_with_model\\Largus', new_name))
