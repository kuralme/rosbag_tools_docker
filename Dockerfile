FROM ros:humble-ros-base-jammy

# Install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends\
    wget curl \
    python3-pip \
    python3-opencv \
    python3-rospy \
    && rm -rf /var/lib/apt/lists/*

RUN pip install bagpy pandas matplotlib rosbags pathlib rosbag-tools

# Copy the scripts from local
COPY ./scripts/* /home/rosbag_tools/
WORKDIR /home/rosbag_tools/
