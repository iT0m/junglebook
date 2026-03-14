# 1. Match your local version (3.14)
FROM python:3.14-slim

# 2. Environment variables for Python performance
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the container's internal folder
WORKDIR /app

# 4. Install Linux tools for PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements first (for faster builds)
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Copy the rest of JungleBook
COPY . /app/