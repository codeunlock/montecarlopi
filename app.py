import numpy as np 
import matplotlib.pyplot as plt

# Function to estimate Pi using Monte Carlo method 
def estimate_pi(num_points):
    #generate the random points in the square for bot x and y 
    x = np.random.uniform(-1,1,num_points)
    y = np.random.uniform(-1,1,num_points)

    #calculate the disctance from the origin for each point
    distance = x**2 + y **2
    #counts how many points fall inside the circle
    inside_circle = distance <= 1
    
    # estimate Pi using the ratio of points inside the circle
    pi_estimate = 4*np.sum(inside_circle) / num_points
    return pi_estimate
#number of random points to generate
num_points = 10000

#estimate pi
pi_value = estimate_pi(num_points)

# Plot 
x = np.random.uniform(-1,1,num_points)
y = np.random.uniform(-1,1,num_points)
distance = x**2 + y ** 2

plt.scatter(x[distance<=1], y[distance<=1], color='blue', s=1)
plt.scatter(x[distance>1], y[distance>1], color='red', s=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f"Monte Carlo Simulation: Estimated Pi = {pi_value}")
plt.show()