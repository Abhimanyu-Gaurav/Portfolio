# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Create a virtual environment
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
