FROM python:3.8
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt
COPY . .

#EXPORT 8000
#CMD ["uvicorn","--host","0.0.0.0", "--port", "8000", "main:app"]

CMD ["uvicorn", "main:app","--host", "0.0.0.0"]