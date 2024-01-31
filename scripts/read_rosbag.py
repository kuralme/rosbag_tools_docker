from pathlib import Path

from rosbags.highlevel import AnyReader

# create reader instance and open for reading
with AnyReader([Path('/home/rosbag_tools/bags/<bag>')]) as reader:
    connections = [x for x in reader.connections if x.topic == '/<topic>']
    for connection, timestamp, rawdata in reader.messages(connections=connections):
         msg = reader.deserialize(rawdata, connection.msgtype)
         print(msg.header.frame_id)