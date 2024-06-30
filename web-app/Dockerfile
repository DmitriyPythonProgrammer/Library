FROM python:3.11

EXPOSE 8000

WORKDIR /library

COPY ./requirements.txt /library/requirements2.txt

RUN pip install --no-cache-dir --upgrade -r /library/requirements2.txt

COPY . /library/web-app

CMD ["fastapi", "run", "web-app/app.py", "--port", "8000", "--host", "0.0.0.0"]