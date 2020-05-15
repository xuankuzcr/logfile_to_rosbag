from core.regulation import Regulation
from geometry_msgs.msg import Vector3Stamped
from geometry_msgs.msg import Vector3
import rospy

def tuple_to_vector3_stamped_msg(match_tuple):
    v = Vector3Stamped()
    
    v.header.stamp = rospy.Time(secs=float(match_tuple[0]))
    v.vector.x = float(match_tuple[1])
    v.vector.y = float(match_tuple[2])
    v.vector.z = float(match_tuple[3])
    ret = (v.header.stamp, v)
    return ret


def vins_additional_regulation():
    regulations = []
    reg_vel = Regulation('/acc_bias')
    reg_vel.patterns = ['ba: \(t,x,y,z\):\s(.*?),(.*?),(.*?),(.*?)\n']
    reg_vel.stamp_msg_callback = tuple_to_vector3_stamped_msg

    regulations += [reg_vel]
    return regulations