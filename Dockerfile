FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir /code
RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install 'uvicorn[standard]'

EXPOSE 80

#COPY ./ /code

WORKDIR /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
