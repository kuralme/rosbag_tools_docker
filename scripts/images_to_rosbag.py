"""Example: Save images as rosbag1."""

import numpy

from rosbags.rosbag1 import Writer
from rosbags.serde import serialize_ros1
from rosbags.typesys.types import builtin_interfaces__msg__Time as Time
from rosbags.typesys.types import sensor_msgs__msg__CompressedImage as CompressedImage
from rosbags.typesys.types import std_msgs__msg__Header as Header

TOPIC = '/camera'
FRAMEID = 'map'

# Contains filenames and their timestamps
IMAGES = [
    ('homer.jpg', 42),
    ('marge.jpg', 43),
]


def save_images() -> None:
    """Iterate over IMAGES and save to output bag."""
    with Writer('output.bag') as writer:
        conn = writer.add_connection(TOPIC, CompressedImage.__msgtype__)

        for path, timestamp in IMAGES:
            message = CompressedImage(
                Header(
                    stamp=Time(
                        sec=int(timestamp // 10**9),
                        nanosec=int(timestamp % 10**9),
                    ),
                    frame_id=FRAMEID,
                ),
                format='jpeg',  # could also be 'png'
                data=numpy.fromfile(path, dtype=numpy.uint8),
            )

            writer.write(
                conn,
                timestamp,
                serialize_ros1(message, CompressedImage.__msgtype__),
            )