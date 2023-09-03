# Указываем базовый образ
FROM python:3.11.4

# Копируем requirements.txt в контекст сборки Docker-образа
COPY requirements.txt /directory_project/requirements.txt

# Устанавливаем зависимости
RUN pip install -r /directory_project/requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . /directory_project

# Устанавливаем рабочую директорию
WORKDIR /directory_project

# Опционально: указываем порт, который будет использоваться при запуске контейнера
EXPOSE 8000

# Опционально: указываем команду, которая будет выполнена при запуске контейнера
CMD ["python", "main.py", "run"]