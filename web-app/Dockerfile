FROM python:3.11

EXPOSE 80

WORKDIR /library

COPY ./requirements.txt /library/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /library/requirements.txt

COPY ./web-app /library/web-app

CMD ["fastapi", "run", "web-app/app.py", "--port", "80", "--host", "0.0.0.0"]