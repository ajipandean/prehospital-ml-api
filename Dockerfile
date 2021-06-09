FROM python:3.8-buster

# Set working director
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8080

CMD ["python", "app.py"]