
import math

steering_track = 1.5
wheel_base_ = 1.830
wheel_radius_ = 0.4
M_PI_2 = math.pi/2.0


# Both should be from 0-1.
def calculate_steering(steer, throttle):

    throttle_cmd = throttle
    angle_cmd = steer * math.radians(45)

    # Limit velocities and accelerations:
    #limiter_lin_.limit(throttle_cmd, last0_cmd_.lin_x, last1_cmd_.lin_x, cmd_dt)
    #limiter_ang_.limit(angle_cmd, last0_cmd_.ang, last1_cmd_.ang, cmd_dt)
    # last1_cmd_ = last0_cmd_
    # last0_cmd_ = curr_cmd_twist

    front_left_steering = 0
    front_right_steering = 0
    rear_left_steering = 0
    rear_right_steering = 0
    vel_left_front = 0
    vel_right_front = 0
    vel_right_rear = 0
    vel_left_rear = 0

    #// Compute wheels velocities:
    if(math.fabs(throttle_cmd) > 0.001):

      vel_steering_offset = 0#(angle_cmd*wheel_steering_y_offset_)/wheel_radius_
      vel_left_front  = throttle_cmd * math.sqrt((math.pow(throttle_cmd - angle_cmd*steering_track/2,2)
                                                                         +math.pow(wheel_base_*angle_cmd/2.0,2)))/wheel_radius_ - vel_steering_offset
      vel_right_front = throttle_cmd * math.sqrt((math.pow(throttle_cmd + angle_cmd*steering_track/2,2)
                                                                         +math.pow(wheel_base_*angle_cmd/2.0,2)))/wheel_radius_ + vel_steering_offset
      vel_left_rear = throttle_cmd * math.sqrt((math.pow(throttle_cmd - angle_cmd*steering_track/2,2)
                                                                       +math.pow(wheel_base_*angle_cmd/2.0,2)))/wheel_radius_ - vel_steering_offset
      vel_right_rear = throttle_cmd * math.sqrt((math.pow(throttle_cmd + angle_cmd*steering_track/2,2)
                                                                        +math.pow(wheel_base_*angle_cmd/2.0,2)))/wheel_radius_ + vel_steering_offset
        # vel_left_front  = math.copysign(1.0, throttle_cmd) * math.sqrt((math.pow(throttle_cmd + angle_cmd*steering_track/2,2)
        #                                                                    +math.pow(wheel_base_*angle_cmd/2.0,2)))/wheel_radius_ - vel_steering_offset
        # vel_right_front = math.copysign(1.0, throttle_cmd) * math.sqrt((math.pow(throttle_cmd - angle_cmd*steering_track/2,2)
        #                                                                    +math.pow(wheel_base_*angle_cmd/2.0,2)))/wheel_radius_ + vel_steering_offset
        # vel_left_rear = math.copysign(1.0, throttle_cmd) * math.sqrt((math.pow(throttle_cmd + angle_cmd*steering_track/2,2)
        #                                                                  +math.pow(wheel_base_*angle_cmd/2.0,2)))/wheel_radius_ - vel_steering_offset
        # vel_right_rear = math.copysign(1.0, throttle_cmd) * math.sqrt((math.pow(throttle_cmd - angle_cmd*steering_track/2,2)
        #                                                                   +math.pow(wheel_base_*angle_cmd/2.0,2)))/wheel_radius_ + vel_steering_offset


    # #// // Compute steering angles
    throttle_cmd = 1.0
    if math.fabs(2.0*throttle_cmd) > math.fabs(angle_cmd*steering_track):
      front_left_steering = math.atan(angle_cmd*wheel_base_ /
                                  (2.0*throttle_cmd + angle_cmd*steering_track))
      front_right_steering = math.atan(angle_cmd*wheel_base_ /
                                   (2.0*throttle_cmd - angle_cmd*steering_track))
      rear_left_steering = -math.atan(angle_cmd*wheel_base_ /
                                  (2.0*throttle_cmd + angle_cmd*steering_track))
      rear_right_steering = -math.atan(angle_cmd*wheel_base_ /
                                   (2.0*throttle_cmd - angle_cmd*steering_track))

    # if angle_cmd!=0:
    #   front_left_steering = math.atan(angle_cmd*wheel_base_ /
    #                               (angle_cmd*steering_track))
    #   front_right_steering = math.atan(angle_cmd*wheel_base_ /
    #                                (angle_cmd*steering_track))
    #   rear_left_steering = -math.atan(angle_cmd*wheel_base_ /
    #                               (angle_cmd*steering_track))
    #   rear_right_steering = -math.atan(angle_cmd*wheel_base_ /
    #                                (angle_cmd*steering_track))

    # elif math.fabs(throttle_cmd) > 0.001:
    #   front_left_steering = math.copysign(M_PI_2, angle_cmd)
    #   front_right_steering = math.copysign(M_PI_2, angle_cmd)
    #   rear_left_steering = math.copysign(M_PI_2, -angle_cmd)
    #   rear_right_steering = math.copysign(M_PI_2, -angle_cmd)

    return {"front_left":(front_left_steering, vel_left_front), "front_right": (front_right_steering, vel_right_front), "rear_left":(rear_left_steering, vel_left_rear), "rear_right": (rear_right_steering, vel_right_rear)}