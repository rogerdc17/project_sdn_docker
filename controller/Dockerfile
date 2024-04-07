# Use an official Python 2.7 slim image as a base
FROM python:3

# Install necessary dependencies for Ryu SDN Controller
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libssl-dev \
    python-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip

RUN pip install ryu

# Create a directory for the controller code
WORKDIR /app

# Copy the controller code into the container
COPY controller.py ./

# Expose the OpenFlow port for controller communication
EXPOSE 6633

# Command to run the controller
CMD ["ryu-manager", "controller.py"]

