FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /my_todo_list

WORKDIR /my_todo_list

ADD . /my_todo_list

RUN pip install -r requirements.txt

