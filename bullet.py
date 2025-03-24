class Bullet:
    def __init__(self, name, weight, diameter, bc, drag_function):
        self.name = name # e.g., "Hornady ELD-X"
        self.weight = weight  # in grains
        self.diameter = diameter  # in inches
        self.bc = bc  # ballistic coefficient
        self.drag_function = drag_function  # e.g., G1, G7

    def __str__(self):
        return f"Bullet(name={self.name}, weight={self.weight}, diameter={self.diameter}, bc={self.bc}, drag_function={self.drag_function})"