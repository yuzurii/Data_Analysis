"""15-1. Cubes: A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5000 cubic numbers.
15-2. Colored Cubes: Apply a colormap to your cubes plot."""
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=3)

# Set title and labels
ax.set_title('Cubic Numbers', fontsize=14)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cubic Values', fontsize=14)

# Set range for each axis
ax.axis([0, 5100, 0, 140_000_000_000])

plt.show()
