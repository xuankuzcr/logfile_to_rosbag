from core.apply_dict import write_stamp_msgs_to_bag
from regulation_dict.kunlun_regulation import get_kunlun_regulations
from regulation_dict.g2o_from_gtsam_regulation import g2o_from_gtsam_regulation
import os
import rosbag
from sys import argv
from geometry_msgs.msg import PoseStamped


def ReadMarkerTfBag(input_bagname):
    input_bag = rosbag.Bag(input_bagname, 'r')
    fid_tf = []
    for topic, msg, t in input_bag.read_messages(topics=['/fiducial_transforms']):
        fid_tf += [msg]
    return fid_tf

def CreatePoseStamped(camera_poses, fid_tf_msgs):
    msgs_offset = 1
    stamped_poses = []
    for i in range(len(camera_poses)):
        pose_stamped = PoseStamped()
        pose_stamped.header = fid_tf_msgs[msgs_offset + i].header
        pose_stamped.pose = camera_poses[i]
        stamped_poses += [[pose_stamped.header.stamp, pose_stamped]]
    return stamped_poses


if __name__ == '__main__':
    if(len(argv) < 3):
        print("example: python traj_from_g2o.py xxx.g2o fiducialtf.bag")
        quit()

    log_filename = argv[1]
    input_bagname = argv[2]
    output_bagname = os.path.splitext(log_filename)[0] + '.bag'
    regulations = g2o_from_gtsam_regulation()

    log_file = open(log_filename, 'r')
    log = log_file.read()

    output_bag = rosbag.Bag(output_bagname, 'w')
    
    fid_tf = ReadMarkerTfBag(input_bagname)

    pose_msgs = regulations[0].apply(log)
    # print(len(pose_msgs))
    stamped_poses = CreatePoseStamped(pose_msgs, fid_tf)
    print(len(stamped_poses))
    write_stamp_msgs_to_bag(output_bag, stamped_poses, regulations[0].topic_name)
    output_bag.close()