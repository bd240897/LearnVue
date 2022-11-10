# образ на основе которого создаём контейнер
FROM python:3.8.6-alpine

# рабочая директория внутри проекта
WORKDIR /home/project/api

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgres
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libc-dev libffi-dev

# matplotlib
RUN apk add g++ jpeg-dev zlib-dev libjpeg make

# skipy
RUN apk add bash openssh curl ca-certificates openssl less htop \
            g++ make wget rsync \
            build-base libpng-dev freetype-dev libexecinfo-dev openblas-dev libgomp lapack-dev \
            libgcc libquadmath musl  \
            libgfortran \
            lapack-dev

# чтобы работала pillow
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

# устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip

# копируем содержимое текущей папки в контейнер
COPY . .
RUN pip install -r req.txt

#RUN python manage.py migrate

RUN chmod +x ./entrypoint.sh
#COPY ./entrypoint.sh ./home/project/api
#ENTRYPOINT ["./entrypoint.sh"]

