from core.regulation import Regulation
from geometry_msgs.msg import Pose
import rospy

def create_pose_from_g2o(match_tuple):
    pose = Pose()
    pose.position.x     = float(match_tuple[1])
    pose.position.y     = float(match_tuple[2])
    pose.position.z     = float(match_tuple[3])
    pose.orientation.x  = float(match_tuple[4])
    pose.orientation.y  = float(match_tuple[5])
    pose.orientation.z  = float(match_tuple[6])
    pose.orientation.w  = float(match_tuple[7])
    return pose

def g2o_from_gtsam_regulation():
    regulations = []
    reg_traj = Regulation('/camera_trajectory')
    reg_traj.patterns = ['VERTEX_SE3:QUAT\s86(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s']
    reg_traj.stamp_msg_callback = create_pose_from_g2o

    regulations += [reg_traj]
    return regulations