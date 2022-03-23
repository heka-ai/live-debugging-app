FROM python:3.8-slim-buster

# Make sure scripts in .local are usable
ENV PATH "${PATH}:/root/.local/bin"

# Copy the source code
COPY requirements.txt /app/requirements.txt
COPY app/app.py /app/app.py
COPY app/.vscode/launch.json /app/.vscode/launch.json

WORKDIR /app

RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]