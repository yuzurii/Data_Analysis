import matplotlib.pyplot as plt

input_values = ["One", "Two", "Three", "Four", "Five"]
squares = [1, 4, 9, 16, 26]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Square of Values", fontsize=14)
ax.set_ylabel("Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()