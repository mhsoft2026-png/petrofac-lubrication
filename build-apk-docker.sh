#!/bin/bash

# Script to build APK using Docker (no Java installation needed)

echo "Building APK using Docker..."

# Create Dockerfile for building
cat > Dockerfile.build << 'EOF'
FROM openjdk:17-slim

# Install Android SDK
RUN apt-get update && apt-get install -y wget unzip git nodejs npm

# Install Android SDK Command Line Tools
ENV ANDROID_SDK_ROOT=/opt/android-sdk
RUN mkdir -p ${ANDROID_SDK_ROOT}/cmdline-tools && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip && \
    unzip commandlinetools-linux-9477386_latest.zip -d ${ANDROID_SDK_ROOT}/cmdline-tools && \
    mv ${ANDROID_SDK_ROOT}/cmdline-tools/cmdline-tools ${ANDROID_SDK_ROOT}/cmdline-tools/latest

ENV PATH=${PATH}:${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin:${ANDROID_SDK_ROOT}/platform-tools

# Accept licenses
RUN yes | sdkmanager --licenses

# Install required packages
RUN sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.0"

WORKDIR /app
COPY . .

# Install dependencies and build
RUN npm install && \
    npm run build && \
    npx cap sync android && \
    cd android && \
    chmod +x gradlew && \
    ./gradlew assembleDebug

CMD ["cp", "android/app/build/outputs/apk/debug/app-debug.apk", "/output/petrofac-lubrication.apk"]
EOF

# Build the Docker image and extract APK
docker build -f Dockerfile.build -t petrofac-builder . && \
docker create --name petrofac-temp petrofac-builder && \
docker cp petrofac-temp:/app/android/app/build/outputs/apk/debug/app-debug.apk ./petrofac-lubrication.apk && \
docker rm petrofac-temp

echo "✓ APK built successfully: petrofac-lubrication.apk"
