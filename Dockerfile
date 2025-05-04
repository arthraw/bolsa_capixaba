# Install Airflow image from docker repository
FROM apache/airflow:3.0.0

USER root

# Configure project level to python recognize all modules
ENV PYTHONPATH="/opt/airflow:${PYTHONPATH}"

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    chromium && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install OpenJDK 11 manually
RUN mkdir -p /usr/lib/jvm && \
    curl -L -o /tmp/openjdk11.tar.gz https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.23+9/OpenJDK11U-jdk_x64_linux_hotspot_11.0.23_9.tar.gz && \
    tar -xzf /tmp/openjdk11.tar.gz -C /usr/lib/jvm && \
    mv /usr/lib/jvm/jdk-11.0.23+9 /usr/lib/jvm/java-11-openjdk-amd64 && \
    rm /tmp/openjdk11.tar.gz


ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Copy environment file
COPY .env /opt/airflow/.env

USER airflow

# Install Python project dependencies
RUN pip install --no-cache-dir \
    python-dotenv~=1.1.0 \
    selenium~=4.31.0 \
    webdriver-manager~=4.0.2 \
    pyspark~=3.5.5 \
    apache-airflow-providers-apache-spark \
    apache-airflow-providers-postgres \
    apache-airflow-providers-microsoft-azure
