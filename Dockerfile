FROM python:3.11.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEVBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/ezra/Documents/Loan-Management-Mania

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000 
