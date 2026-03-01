import math

g = 9.8  # gravity constant

velocity = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter launch angle (degrees): "))

angle_rad = math.radians(angle)

# Time of flight
time = (2 * velocity * math.sin(angle_rad)) / g

# Maximum height
height = (velocity**2 * math.sin(angle_rad)**2) / (2 * g)

# Range
range_projectile = (velocity**2 * math.sin(2 * angle_rad)) / g

print("\n--- Projectile Motion Results ---")
print("Time of Flight:", round(time, 2), "seconds")
print("Maximum Height:", round(height, 2), "meters")
print("Range:", round(range_projectile, 2), "meters")
print("\nThis simulation demonstrates basic trajectory modelling used in aerospace systems.")