# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the working directory
COPY . .

# Run tests
# RUN pytest tests/
EXPOSE 5000
# Set the entrypoint command to run the Python script
CMD ["python", "app.py"]