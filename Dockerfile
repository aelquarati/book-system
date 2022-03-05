FROM python:3.8-alpine

ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 5050

CMD ["flask", "run"]