FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install google.generativeai flask

# Expose the application port
EXPOSE 5000

# Start the Flask web server
CMD ["python", "app.py"]
