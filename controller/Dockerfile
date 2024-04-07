# Use an official Python 3 slim image as a base
FROM python:3

# Install necessary dependencies for Ryu SDN Controller
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install Ryu
RUN pip install ryu

# Copy the controller code into the container
COPY controller.py /

# Expose the OpenFlow port for controller communication
EXPOSE 6633

# Command to run the controller in interactive mode
CMD ["python3", "-i", "controller.py"]
