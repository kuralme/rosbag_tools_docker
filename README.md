# Rosbag Tools Docker

Several useful scripts for ros1 and ros2 bags build in a containerised environment. Mostly obtained from the examples of the [API](https://ternaris.gitlab.io/rosbags/).

| Script                | Description                             |
|:----------------------|:----------------------------------------|
| `bag_to_table.py`     | Extract data to a csv table
| `read_rosbag.py`      | Read topics of ROS1 bag
| `read_rosbag2.py`     | Read topics of ROS2 bag
| `write_rosbag2.py`    | Write new topic into a ROS2 bag
| `remove_topic.py`     | Remove topics from ROS2 bag
| `images_to_rosbag.py` | Make a ROS1 bag with images
| `images_to_rosbag2.py`| Make a ROS2 bag with images
| `bag_to_images.py`    | Extract images from a ROS bag topic
| `bag_to_video.py`     | Convert images in a rosbag to a variable framerate video.
<!-- | `video_to_bag.py`     | convert a video file to a ROS bag -->

## Rosbag API
Convert "input.bag", save the result as "output.bag"
```
rosbags-convert input.bag --dst /path/to/output.bag
```
## Rosbag-tools
Another third-party tools for rosbag manipulations.
```
rosbag-tools `command` <options>
```
Commands:
- clip
- split
- compute-duration
- export-odometry
- topic-compare
- topic-remove

