FROM python:3

WORKDIR /parser_task

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /parser_task

CMD [ "python", "./main.py" ]