# syntax=docker/dockerfile:1

# ---- BASE IMAGE ----
FROM python:3.10-slim as base

# Set environment variables để giảm warning và chạy logs realtime
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- SYSTEM UPDATE ----
# Update security packages & cleanup to avoid cached apt lists
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ---- APP SETUP ----
WORKDIR /app
COPY . .

# ---- INSTALL PYTHON DEPENDENCIES ----
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---- EXPOSE & ENTRY ----
EXPOSE 5000
CMD ["python", "app.py"]
