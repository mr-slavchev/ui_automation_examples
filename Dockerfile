# Use the Playwright image as the base image
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set the working directory to /ui-tests
WORKDIR /ui-tests

# Copy the current directory contents into the container at /ui-tests
COPY . /ui-tests

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint to run pytest
ENTRYPOINT ["pytest"]

