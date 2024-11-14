FROM python:3.8

# Çalışma dizini
WORKDIR /app

# Script
COPY python.py .

# gereksinimler
RUN pip install requests

# calistir
CMD ["python", "python.py"]

