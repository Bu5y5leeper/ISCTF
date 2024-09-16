FROM python:3.10-slim

RUN pip install --index-url https://pypi.org/simple Flask

WORKDIR /app

COPY . .

RUN chmod 445 -R ../app && useradd -ms /bin/bash task_user

USER task_user

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["python", "app.py"]
