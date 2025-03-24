class Environment:
    def __init__(self, wind_speed, wind_direction, temperature, humidity, pressure, altitude):
        self.wind_speed = wind_speed  # in mph
        self.wind_direction = wind_direction  # in degrees (0-360)
        self.temperature = temperature  # in Fahrenheit
        self.humidity = humidity  # as percentage
        self.pressure = pressure  # in inches Hg
        self.altitude = altitude  # in feet
        # Could calculate air density here if desired
        self.air_density = self.calculate_air_density()
    
    def calculate_air_density(self):
        # Placeholder for air density formula based on temp, pressure, humidity, altitude
        pass

    def __str__(self):
        return f"Environment(wind_speed={self.wind_speed}, wind_direction={self.wind_direction}, temperature={self.temperature}, humidity={self.humidity}, pressure={self.pressure}, altitude={self.altitude})"