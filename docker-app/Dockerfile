
# 1. Base image
FROM python:3.11-slim

# 2. Working directory
WORKDIR /app

# 3. Copy dependencies first
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY . .

# 6. Expose port
EXPOSE 5000

# 7. Start application
CMD ["python", "app.py"]
