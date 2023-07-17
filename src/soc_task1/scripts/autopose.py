#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy

from soc_task1.srv import fibonacci

def fib_client(x):
    rospy.wait_for_service('Fibonacci')
    try:
        fibonacci_n = rospy.ServiceProxy('Fibonacci', fibonacci)
        resp = fibonacci_n(x)
        return resp.fib
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def usage():
    return "%s [x]"%sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s"%x)
    print("Fibonacci[%s] = %s"%(x, fib_client(x)))