import anki_vector

# Create a Robot object
robot = anki_vector.Robot()
# Connect to the Robot
robot.connect()
# Custom commands
robot.behavior.drive_straight(distance_mm(200), speed_mmps(100))

# Disconnect from Vector
robot.disconnect()
