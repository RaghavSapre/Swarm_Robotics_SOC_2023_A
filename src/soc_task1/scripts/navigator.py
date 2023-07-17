#! /usr/bin/env python3

from __future__ import print_function
from soc_task1.srv import fibonacci,fibonacciResponse
import rospy

def fib(x):
    if(x == 1):
        return 0
    if(x == 2):
        return 1
    else:
        a = 0
        b = 1
        for _ in range(3, x+1):
                b = a + b
                a = b - a
        return b

def handle_fibonacci(req):
    print("Returning {Fibonacci[%s] = %s}"%(req.a, fib(req.a)))
    return fibonacciResponse(fib(req.a))

def fibonacci_server():
    rospy.init_node('navigator', anonymous=True)
    rospy.Service('Fibonacci', fibonacci, handle_fibonacci)
    print("Ready to give Fibonacci[n].")
    rospy.spin()

if __name__ == '__main__':
    fibonacci_server()