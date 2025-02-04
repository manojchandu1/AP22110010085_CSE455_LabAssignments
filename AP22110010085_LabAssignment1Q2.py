class TemperatureControlAgent:
    def __init__(self, desired_temp, tolerance):
        self.desired_temp = desired_temp
        self.tolerance = tolerance
        self.current_temp = desired_temp  # Initial assumption

    def sense_temperature(self, temp):
        """ Updates the current temperature based on sensor input. """
        self.current_temp = temp

    def decide_action(self):
        """ Determines whether to heat, cool, or do nothing. """
        if self.current_temp < self.desired_temp - self.tolerance:
            return "Turn on Heating"
        elif self.current_temp > self.desired_temp + self.tolerance:
            return "Turn on Cooling"
        else:
            return "Maintain Temperature"

# Example usage
agent = TemperatureControlAgent(desired_temp=22, tolerance=1)

temperatures = [20, 21, 22, 23, 24]
for temp in temperatures:
    agent.sense_temperature(temp)
    action = agent.decide_action()
    print(f"Current Temp: {temp}°C -> Action: {action}")
