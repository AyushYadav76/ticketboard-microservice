# Use full Python 3.13 image (includes build tools)
FROM python:3.13

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

# Optional: Remove build tools to reduce size (if needed)
# RUN apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]