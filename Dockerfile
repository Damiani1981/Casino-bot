FROM python:3.9  
WORKDIR /app  
COPY . /app  
RUN pip install --no-cache-dir -r requirements.txt || true  
CMD ["python3", "ultimo_backup_perfecto.py"]
