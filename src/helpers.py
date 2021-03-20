from math import pi
def total_rotational_increment(old_dir, new_dir):
    """
    old_dir: from which dir it's coming (cardinal).
    new_dir: to which dir it's going (cardinal).
    returns: The difference in radians between the two rotations.
    """
    if old_dir == "up":
            if new_dir == "right":
                return -pi/2
            elif new_dir == "down":
                self.radians += 2*pi/2
            elif new_dir == "left":
                self.radians += pi/2
        elif old_dir == "right":
            if new_dir == "up":
                self.radians += pi/2
            elif new_dir == "down":
                self.radians -= pi/2
            elif new_dir == "left":
                self.radians -= 2*pi/2
        elif old_dir == "down":
            if new_dir == "right":
                self.radians += pi/2
            elif new_dir == "up":
                self.radians -= 2*pi/2
            elif new_dir == "left":
                self.radians -= pi/2
        elif old_dir == "left":
            if new_dir == "right":
                self.radians += 2*pi/2
            elif new_dir == "down":
                self.radians += pi/2
            elif new_dir == "up":
                self.radians -= pi/2