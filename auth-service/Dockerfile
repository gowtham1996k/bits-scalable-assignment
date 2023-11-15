# Use a base image with Python and Flask
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP 'app.py'
ENV FLASK_DEBUG 1


# Set the working directory in the container
WORKDIR /auth-service

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 5005

# Command to run the application
CMD ["flask", "run"]
