FROM python:3.7

RUN pip3 install flask requests

COPY . . 

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]