import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('ThesisResults.xlsx')

# Create a new figure and two subplots (2 rows, 1 column)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))

# Create x-axis time range
time = range(1, len(df) + 1)

# Plot traditional and smart traffic light times for pedestrians
ax1.plot(time, df['Traditional TrafficLight Pedestrian Time'], label='Traditional', color='blue', marker='o')
ax1.plot(time, df['Smart TrafficLight Pedestrian Time'], label='Smart', color='red', marker='o')

# Label every 10th point
for i, txt in enumerate(df['Traditional TrafficLight Pedestrian Time']):
    if i % 5 == 0:
        ax1.annotate(txt, (time[i], df['Traditional TrafficLight Pedestrian Time'][i]), 
                     xytext=(-20,25), textcoords='offset points', 
                     arrowprops=dict(arrowstyle='->'))

for i, txt in enumerate(df['Smart TrafficLight Pedestrian Time']):
    if i % 5 == 0:
        ax1.annotate(txt, (time[i], df['Smart TrafficLight Pedestrian Time'][i]), 
                     xytext=(-20,25), textcoords='offset points',
                     arrowprops=dict(arrowstyle='->'))

ax1.set_xticks(time)  # sets the x-axis ticks
ax1.set_yticks([])  # removes the y-axis ticks
ax1.set_title('Traffic Light Times for Pedestrians')
ax1.legend()

# Plot traditional and smart traffic light times for vehicles
ax2.plot(time, df['Traditional TrafficLight Vehicle Time'], label='Traditional', color='blue', marker='o')
ax2.plot(time, df['Smart TrafficLight Vehicle Time'], label='Smart', color='red', marker='o')

# Label every 10th point
for i, txt in enumerate(df['Traditional TrafficLight Vehicle Time']):
    if i % 10 == 0:
        ax2.annotate(txt, (time[i], df['Traditional TrafficLight Vehicle Time'][i]),
                     xytext=(-20,25), textcoords='offset points',
                     arrowprops=dict(arrowstyle='->'))

for i, txt in enumerate(df['Smart TrafficLight Vehicle Time']):
    if i % 10 == 0:
        ax2.annotate(txt, (time[i], df['Smart TrafficLight Vehicle Time'][i]),
                     xytext=(-20,25), textcoords='offset points',
                     arrowprops=dict(arrowstyle='->'))

ax2.set_xticks(time)  # sets the x-axis ticks
ax2.set_yticks([])  # removes the y-axis ticks
ax2.set_title('Traffic Light Times for Vehicles')
ax2.legend()

# Set common x-axis label
plt.xlabel('Time')

# Show plot
plt.tight_layout()
plt.show()
