#!/usr/bin/env python3
import sys
import rospy
from inverted_pendulum_sim.srv import SetParams
from inverted_pendulum_sim.srv import SetParamsRequest
from inverted_pendulum_sim.srv import SetParamsResponse

def set_parameters_client(m, l, m_c, th, th_d, th_dd, x, x_d, x_dd):
    rospy.wait_for_service('set_parameters')
    try:
        set_parameters = rospy.ServiceProxy('/inverted_pendulum/set_params', SetParams)
        resp1 = set_parameters(m, l, m_c, th, th_d, th_dd, x, x_d, x_dd)
        return resp1
    except rospy.ServiceException(e):
        print ("Service call failed: %s"%e)

def usage():
    return 

if __name__ == "__main__":
    if len(sys.argv) == 10:
        pendulum_mass = int(sys.argv[1])
        pendulum_length = int(sys.argv[2])
        cart_mass = float(sys.argv[3])
        theta_0 = int(sys.argv[4])
        theta_dot = int(sys.argv[5])
        th_d_dot = int(sys.argv[6])
        x = int(sys.argv[7])
        x_dot = int(sys.argv[8])
        x_d_dot = int(sys.argv[9])
    else:
        print ("%s "%sys.argv[0])
        sys.exit(1)
    print ("Requesting to set parameters")

