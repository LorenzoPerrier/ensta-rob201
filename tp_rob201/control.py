""" A set of robotics control functions """
import numpy as np
import random


def reactive_obst_avoid(lidar):
    """
    Simple obstacle avoidance
    lidar : placebot object with lidar data
    """
    # TODO for TP1
    dist = lidar.get_sensor_values()
    angles = lidar.get_ray_angles()
    delta = 2*np.pi

    # Check if object in front
    frontObject = False
    # indexTable = [i for i in range(0, len(dist)) if abs(angles[i]) < delta]
    # distTable = dist[indexTable]
    # for elem in distTable:
    #     if elem < 100:
    #         frontObject = True

    # if (frontObject):
    #     if (dist[len(dist)//2] > 20):
    #         maxDistanceIndex = np.argmax(dist)
    #         rotation = angles[maxDistanceIndex] / (2*np.pi)
    #         command = {"forward": 0.5,
    #                    "rotation": rotation}
    #     else:
    #         rotation = random.randint(-180, 180)/180
    #         command = {"forward": -0.5,
    #                    "rotation": rotation}
    # else:
    #     command = {"forward": 0.5,
    #                "rotation": 0}

    maxDistanceIndex = np.argmax(dist)
    minDistance = np.min(dist)
    rotation = angles[maxDistanceIndex] / (2*np.pi)
    if minDistance < 10:
        command = {"forward": 0,
                   "rotation": rotation}
    else:
        command = {"forward": 0.5,
                   "rotation": rotation}
    return command


def potential_field_control(lidar, pose, goal):
    """
    Control using potential field for goal reaching and obstacle avoidance
    lidar : placebot object with lidar data
    pose : [x, y, theta] nparray, current pose in odom or world frame
    goal : [x, y, theta] nparray, target pose in odom or world frame
    """
   # TODO for TP2

    command = {"forward": 0,
               "rotation": 0}

    return command
