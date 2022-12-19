FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY backend/ /app
# docker on sqlite
#CMD ["python3", "manage.py", "runserver", "0:8000"]

#docker-compose with postgres and gunicogn
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ] 
