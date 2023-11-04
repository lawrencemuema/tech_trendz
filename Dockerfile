# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /src

# Copy requirements.txt
COPY packages.txt ./

# Install dependencies
RUN pip install -r packages.txt

# Copy the rest of the application source code from the app/ directory
COPY src/ .

# Expose the application port
EXPOSE 8000

# Set the startup command
CMD ["python", "app.py"]
