#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Extract images from a rosbag."""

import argparse
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
from sensor_msgs.msg import Image, CompressedImage
from custom_cvbridge import CvBridge


def main():
    """Extract a folder of images from a rosbag."""
    compressed = True
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file", help="Input ROS bag.")
    parser.add_argument("output_dir", help="Output directory.")
    parser.add_argument("image_topic", help="Image topic.")

    args = parser.parse_args()

    print("Extract images from",args.bag_file,"on topic",args.image_topic,"into ", args.output_dir)
    bag = bagreader(args.bag_file)
    bridge = CvBridge()

    img_msg = bag.message_by_topic(args.image_topic)
    
    for msg in img_msg:
        if compressed:
            cv_img = bridge.compressed_imgmsg_to_cv2(msg, encoding="passthrough")
    csv_image = pd.read_csv(cv_img)
    print(csv_image)

    return

if __name__ == '__main__':
    main()

