class Rifle:
    def __init__(self, name, muzzle_velocity, barrel_twist, sight_height, zero_range):
        self.name = name # e.g., "Ruger Precision Rifle"
        self.muzzle_velocity = muzzle_velocity  # in fps
        self.barrel_twist = barrel_twist  # e.g., 1:7 (could be a float or tuple)
        self.sight_height = sight_height  # in inches
        self.zero_range = zero_range  # in yards

    def __str__(self):
        return f"Rifle(name={self.name}, muzzle_velocity={self.muzzle_velocity}, barrel_twist={self.barrel_twist}, sight_height={self.sight_height}, zero_range={self.zero_range})"