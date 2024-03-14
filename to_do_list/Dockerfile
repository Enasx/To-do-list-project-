# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the local contents into the /app directory in the container
COPY . /app

# Install FastAPI, Uvicorn, and SQLAlchemy dependencies
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install sqlalchemy

# Specify the default command to run when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

