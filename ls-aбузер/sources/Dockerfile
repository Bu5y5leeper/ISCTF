FROM python:3.10-slim

RUN pip install --index-url https://pypi.org/simple Flask

WORKDIR /app

COPY . .

RUN echo FLAG{CAT_ILI_NE_CAT_VOT_V_CHEM_VOPROS} > ./.flag.txt && chmod 445 -R . && useradd -ms /bin/bash task_user

USER task_user

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["python", "app.py"]
