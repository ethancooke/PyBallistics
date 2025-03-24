class Target:
    def __init__(self, distance, angle):
        self.distance = distance  # in yards
        self.angle = angle  # in degrees (inclination)


    def __str__(self):
        return f"Target(distance={self.distance}, angle={self.angle})"