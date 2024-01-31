#!/usr/bin/env python
# coding=utf-8

from sensor_msgs.msg import Image, CompressedImage
import numpy as np
import sys
import rospy
import cv2

class CvBridge:
    def cv2_to_imgmsg(self, cv_image, encoding='bgr8'):
        if encoding == 'rgb8':
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
            encoding = 'bgr8'
        
        img_msg = Image()
        img_msg.height = cv_image.shape[0]
        img_msg.width = cv_image.shape[1]
        img_msg.encoding = encoding
        img_msg.is_bigendian = 0
        img_msg.data = cv_image.tobytes()
        img_msg.step = len(img_msg.data) // img_msg.height

        return img_msg
    
    def cv2_to_compressed_imgmsg(self, cv_image, encoding='bgr8'):
        if encoding == 'rgb8':
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
            encoding = 'bgr8'
        
        _, compressed_img = cv2.imencode('.jpeg', cv_image, [cv2.IMWRITE_JPEG_QUALITY, 90])

        # Create a ROS CompressedImage message and set its fields
        compressed_img_msg = CompressedImage()
        compressed_img_msg.header.stamp = rospy.Time.now()
        compressed_img_msg.format = "jpeg"
        compressed_img_msg.data = compressed_img.tobytes()
        
        return compressed_img_msg
    
    def imgmsg_to_cv2(self, img_msg, encoding='bgr8'):
        dtype = np.dtype('uint8')  # Hardcode to 8 bits...
        dtype = dtype.newbyteorder('>' if img_msg.is_bigendian else '<')
        image_opencv = np.ndarray(shape=(img_msg.height, img_msg.width, 3),
                                  # and three channels of data. Since OpenCV works with bgr natively,
                                  #  we don't need to reorder the channels.
                                  dtype=dtype, buffer=img_msg.data)
        # If the byt order is different between the message and the system.
        if img_msg.is_bigendian == (sys.byteorder == 'little'):
            image_opencv = image_opencv.byteswap().newbyteorder()
        
        if encoding == 'bgr8':
            return image_opencv
        elif encoding == 'rgb8':
            return cv2.cvtColor(image_opencv, cv2.COLOR_BGR2RGB)
    
    def compressed_imgmsg_to_cv2(self, img_msg, encoding="bgr8"):
        """
        Decompresses a compressed image message to a CV2 image.
        :param img_msg: The compressed image message to be converted.
        :type img_msg: sensor_msgs.msg.CompressedImage
        :param desired_encoding: The desired encoding of the image.
        :type desired_encoding: str
        :return: The converted CV2 image.
        :rtype: numpy.ndarray
        """
        
        try:
            np_arr = np.fromstring(img_msg.data, np.uint8)
            cv_image = cv2.imdecode(np_arr, cv2.IMREAD_UNCHANGED)
        except Exception as e:
            raise print(f"[Exception] Occured as {e} in image conversion!")
        
        if encoding == 'bgr8':
            return cv_image
        elif encoding == 'rgb8':
            return cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)