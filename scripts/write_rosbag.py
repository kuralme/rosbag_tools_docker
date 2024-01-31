from rosbags.rosbag2 import Writer
from rosbags.serde import serialize_cdr
from rosbags.typesys.types import std_msgs__msg__String as String

# create writer instance and open for writing
with Writer('/home/rosbag_tools/bags/<bag>') as writer:
    # add new connection
    topic = '/chatter'
    msgtype = String.__msgtype__
    connection = writer.add_connection(topic, msgtype, 'cdr', '')

    # serialize and write message
    timestamp = 42
    message = String('hello world')
    writer.write(connection, timestamp, serialize_cdr(message, msgtype))