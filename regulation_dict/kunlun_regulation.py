from core.regulation import Regulation
# from geometry_msgs.msg import Vector3Stamped
from geometry_msgs.msg import Vector3
import rospy

def create_reg_vel_msg(match_tuple):
    v = Vector3()
    v.x = float(match_tuple[0])
    v.y = float(match_tuple[1])
    v.z = float(match_tuple[2])
    ret = (rospy.Time(match_tuple[0]), v)
    return ret


def get_kunlun_regulations():
    regulations = []
    reg_vel = Regulation('/velocity')
    # reg_vel.patterns = ['^v:\s\((.*?),(.*?),(.*?)\)']
    reg_vel.patterns = ['relative time:\s(.*?)$(\n|.)*?^v:\s\((.*?),(.*?),(.*?)\)']
    reg_vel.stamp_msg_callback = create_reg_vel_msg

    regulations += [reg_vel]
    return regulations