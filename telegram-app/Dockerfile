FROM python:3.11

# set work directory
WORKDIR /library

# install dependencies
COPY ./requirements.txt /library/requirements1.txt
RUN pip install --no-cache-dir --upgrade -r /library/requirements1.txt

# copy project
COPY . /library/telegram-app

# run app
CMD ["python3", "telegram-app/app.py"]