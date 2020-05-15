import re
from regulation import Regulation
import rosbag


def write_stamp_msgs_to_bag(bag, stamp_msg_list, topic_name):
    # print(stamp_msg_list)
    for timestamp, msg in stamp_msg_list:
        bag.write(topic_name, msg, timestamp)
    # pass

def process(log_filename, regulation_table, output_bagname):
    log_file = open(log_filename, 'r')
    log = log_file.read()
    bag = rosbag.Bag(output_bagname, 'w')

    for regulation in regulation_table:
        stamp_msgs = regulation.apply(log)
        write_stamp_msgs_to_bag(bag, stamp_msgs, regulation.topic_name)
    
    bag.close()


