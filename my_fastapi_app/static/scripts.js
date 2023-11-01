const fileInput = document.getElementById('file-input');
const imagePreview = document.getElementById('image-preview');
const dropText = document.getElementById('drop-text');
const submitButton = document.getElementById('submit-button');
const resultContainer = document.createElement('div');
document.body.appendChild(resultContainer);
resultContainer.style.marginTop = '20px';
const loader = createLoader();
loader.style.zIndex = '1000';
document.body.appendChild(loader);
loader.style.display = 'none';

// Создаем фоновый элемент
const overlay = document.createElement('div');
overlay.style.position = 'fixed';
overlay.style.top = '0';
overlay.style.left = '0';
overlay.style.width = '100%';
overlay.style.height = '100%';
overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)'; // Полупрозрачный серый фон
overlay.style.zIndex = '999'; // Значение z-index, чтобы фон был над всеми остальными элементами
document.body.appendChild(overlay)
overlay.style.display = 'none'

let selectedFile;

fileInput.addEventListener('change', () => {
    const files = fileInput.files;

    if (files.length > 0) {
        selectedFile = files[0];
        const reader = new FileReader();
        reader.onload = function (event) {
            const image = new Image();
            image.src = event.target.result;
            imagePreview.innerHTML = ''; // Очищаем предыдущий превью
            imagePreview.appendChild(image);
            imagePreview.classList.remove('hidden');
            dropText.style.display = 'none';
            fileInput.value = null; // Очищаем значение поля ввода
            fileInput.style.height = `${image.height}px`; // Устанавливаем высоту поля
            submitButton.removeAttribute('disabled'); // Разблокируем кнопку
        };
        reader.readAsDataURL(files[0]);
    }
});

imagePreview.addEventListener('click', () => {
    fileInput.click();
});

imagePreview.addEventListener('dragover', (e) => {
    e.preventDefault();
    imagePreview.style.backgroundColor = '#e2e2e2';
});

imagePreview.addEventListener('dragleave', () => {
    imagePreview.style.backgroundColor = '#ffffff';
});

imagePreview.addEventListener('drop', (e) => {
    e.preventDefault();
    imagePreview.style.backgroundColor = '#ffffff';
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        const reader = new FileReader();
        reader.onload = function (event) {
            const image = new Image();
            image.src = event.target.result;
            imagePreview.innerHTML = ''; // Очищаем предыдущий превью
            imagePreview.appendChild(image);
            imagePreview.classList.remove('hidden');
            dropText.style.display = 'none';
            fileInput.style.height = `${image.height}px`; // Устанавливаем высоту поля
            submitButton.removeAttribute('disabled'); // Разблокируем кнопку
        };
        reader.readAsDataURL(files[0]);
    }
});

submitButton.addEventListener('click', () => {
    if (!submitButton.hasAttribute('disabled')) {
        loader.style.display = 'block';
        overlay.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Блокируем прокрутку страницы
        let applicationId; // Переменная для хранения applicationId

        if (!selectedFile) {
            console.error('Файл не выбран');
            loader.style.display = 'none';
            overlay.style.display = 'none';
            document.body.style.overflow = 'auto'; // Разблокируем прокрутку страницы
            document.body.style.backgroundColor = 'transparent'; // Восстанавливаем фон

            return;
        }
        // Здесь выполняйте последовательные запросы
        performRequest1()
            .then(data => {
                applicationId = data.applicationId;
                // Получен applicationId
                console.log(`Получен applicationId: ${applicationId}`);
                // const formData = new FormData();
                // formData.append('file', selectedFile, selectedFile.name);
                return performRequest2(applicationId, selectedFile);
            })
            .then(() => {
                return performRequest3(applicationId);
            })
            .then(() => {
                return pollForStatus(applicationId);
            })
            .then(() => {
                // Запрос №5
                return performRequest5(applicationId);
            })
            .then(response => {
                // Получены результаты
                console.log(`Получены результаты: ${response}`);
                loader.style.display = 'none';
                overlay.style.display = 'none';
                document.body.style.overflow = 'auto'; // Разблокируем прокрутку страницы
                document.body.style.backgroundColor = 'transparent'; // Восстанавливаем фон

            })
            .catch(error => {
                console.error(error);
                loader.style.display = 'none';
                overlay.style.display = 'none';
                document.body.style.overflow = 'auto'; // Разблокируем прокрутку страницы
                document.body.style.backgroundColor = 'transparent'; // Восстанавливаем фон
            });
    }
});

// Функция для выполнения запроса №1
function performRequest1() {
    return fetch('http://127.0.0.1:8001/api/v1/public/detection/application/create', {
        method: 'POST'
    })
        .then(response => response.json())
        .then(data => {
            if (data && data.applicationId) {
                return data; // Вернуть данные
            } else {
                throw new Error('Ошибка при создании заявки');
            }
        });
}

// Функция для выполнения запроса №2 (загрузка изображения в кодировке base64)
function performRequest2(applicationId, file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();

        reader.onload = function () {
            const base64Image = reader.result.split(',')[1]; // Получаем содержимое файла в base64

            // Теперь отправляем запрос с base64Image в теле запроса
            fetch(`http://127.0.0.1:8001/api/v1/public/detection/${applicationId}/file`, {
                method: 'POST',
                body: JSON.stringify({"fileBase64": base64Image}), // Отправляем base64 изображения
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (response.ok) {
                        resolve();
                    } else {
                        reject('Ошибка при загрузке изображения');
                    }
                })
                .catch(error => {
                    reject(error);
                });
        };

        reader.readAsDataURL(file); // Преобразуем файл в base64
    });
}


// Функция для выполнения запроса №3
function performRequest3(applicationId) {
    return fetch(`http://127.0.0.1:8001/api/v1/public/detection/${applicationId}/send`, {
        method: 'POST'
    })
        .then(response => response.json())
}

// Функция для выполнения запроса №4 (проверка статуса)
function pollForStatus(applicationId) {
    return new Promise((resolve, reject) => {
        const interval = setInterval(() => {
            fetch(`http://127.0.0.1:8001/api/v1/public/detection/${applicationId}/status`, {method: 'GET'})
                .then(response => response.json())
                .then(data => {
                    if (data.status === 2 || data.status === 3) {
                        clearInterval(interval);
                        resolve();
                    }
                })
                .catch(error => {
                    clearInterval(interval);
                    reject(error);
                });
        }, 2000); // Проверка каждые 2 секунды
    });
}

// Функция для выполнения запроса №5
function performRequest5(applicationId) {
    return fetch(`http://127.0.0.1:8001/api/v1/public/detection/${applicationId}/result`, {method: 'GET'})
        .then(response => response.json())
        .then(result => {
            // Получены результаты
            console.log(`Получены результаты: ${JSON.stringify(result)}`);

            if (!result.isCar) {
                const notDetectedText = document.createElement('div');
                notDetectedText.innerText = 'На фото не обнаружен автомобиль';
                notDetectedText.style.fontSize = '24px'; // Устанавливаем размер шрифта
                notDetectedText.style.marginTop = '10px'; // Добавляем отступ сверху
                imagePreview.insertBefore(notDetectedText, imagePreview.firstChild);
            } else {
                const boxes = JSON.parse(result.result).boxes;
                const classes = JSON.parse(result.result).classes;
                const prices = generateRandomPrices(classes);
                drawBoundingBoxes(selectedFile, boxes, classes);

                const table = createTable(classes, prices);
                resultContainer.appendChild(table);
            }
        })
        .catch(error => {
            console.error(error);
        });
}

function drawBoundingBoxes(imageFile, boxes, classes) {
    const image = new Image();
    image.src = URL.createObjectURL(imageFile);

    image.onload = () => {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        canvas.width = image.width;
        canvas.height = image.height;
        context.drawImage(image, 0, 0, image.width, image.height);

        const colors = ['red', 'blue', 'green', 'orange', 'purple']; // Пример цветов

        for (let i = 0; i < boxes.length; i++) {
            const box = boxes[i];
            const className = classes[i];
            const color = colors[i % colors.length]; // Цвет из массива colors

            context.strokeStyle = color; // Устанавливаем цвет рамки
            context.lineWidth = 4; // Устанавливаем толщину линии
            context.rect(box[0], box[1], box[2], box[3]);
            context.stroke();

            context.fillStyle = color; // Устанавливаем цвет текста
            context.font = 'bold 20px Arial'; // Устанавливаем шрифт и размер текста
            context.fillText(className, box[0], box[1] - 10); // Рисуем текст над рамкой
        }

        const imageWithBoundingBoxes = new Image();
        imageWithBoundingBoxes.src = canvas.toDataURL('image/jpeg');
        imagePreview.innerHTML = ''; // Очищаем предыдущее изображение
        imagePreview.appendChild(imageWithBoundingBoxes);
    };
}

function generateRandomPrices(classes) {
    // Генерация рандомных цен для каждого класса
    const prices = {};
    for (const className of classes) {
        prices[className] = (Math.random() * 1000 + 500).toFixed(2); // Пример рандомных цен
    }
    return prices;
}

function createTable(classes, prices) {
    const table = document.createElement('table');
    const thead = table.createTHead();
    const tbody = table.createTBody();

    const headRow = thead.insertRow();
    const th1 = document.createElement('th');
    const th2 = document.createElement('th');
    th1.textContent = 'Повреждение';
    th2.textContent = 'Цена ремонта';
    headRow.appendChild(th1);
    headRow.appendChild(th2);

    for (const className of classes) {
        const row = tbody.insertRow();
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        cell1.textContent = className;
        cell2.textContent = prices[className];
    }

    table.style.marginTop = '20px'; // Добавляем отступ перед таблицей
    return table;
}

function createLoader() {
    const loader = document.createElement('div');
    loader.innerHTML = '<div class="spinner"></div>'; // Крутящийся лоадер
    loader.style.display = 'block';
    loader.style.position = 'fixed';
    loader.style.top = '50%';
    loader.style.left = '50%';
    loader.style.transform = 'translate(-50%, -50%)';
    loader.style.backgroundColor = 'rgba(255, 255, 255, 0.8)';
    loader.style.padding = '20px';
    loader.style.borderRadius = '10px';
    return loader;
}

