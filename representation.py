import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def motion_hover(event):
    # We want to toggle the visibility so we need to know where we start
    is_visible = annotation.get_visible()

    # Check if the mouse pointer is within the plot area
    if event.inaxes == ax:
        # Check if the mouse pointer is over a dot
        is_in, annotation_index = scatter.contains(event)
        if is_in:
            # Get info about the dot
            data_point = scatter.get_offsets()[annotation_index['ind'][0]]
            annotation.xy = data_point

            # Format the label text
            text_label = f'GPA: {data_point[1]}\nHours Studied per week: {data_point[0]}'

            # Attach and show the label
            annotation.set_text(text_label)
            annotation.set_visible(True)
            fig.canvas.draw_idle()
        else:
            # Turn off the label if you are not on a dot
            if is_visible:
                annotation.set_visible(False)
                fig.canvas.draw_idle()

# Load data from csv files
with open("gpastudyhours2.csv", newline='') as studyhours2:
    reader = csv.reader(studyhours2)
    studyhours2 = list(reader)

with open("gpastudyhours3.csv", newline='') as studyhours3:
    reader = csv.reader(studyhours3)
    studyhours3 = list(reader)

with open("gpastudyhours4.csv", newline='') as studyhours4:
    reader = csv.reader(studyhours4)
    studyhours4 = list(reader)

# Process data
i = 1
while i < len(studyhours3):
    value = float(studyhours3[i][1])
    value = round(value / 100 * 4, 2)
    studyhours3[i][1] = value
    i += 1

allStudents = []
i = 1

while i < len(studyhours2):
    if studyhours2[i][0] and studyhours2[i][1]:
        allStudents.append([float(studyhours2[i][1]), float(studyhours2[i][0])])
        i += 1

i = 1

while i < len(studyhours3):
    if studyhours3[i][0] and studyhours3[i][1]:
        allStudents.append([float(studyhours3[i][0]), float(studyhours3[i][1])])
    i += 1

i = 1

while i < len(studyhours4):
    if studyhours4[i][0] and studyhours4[i][1]:
        allStudents.append([float(studyhours4[i][1]), float(studyhours4[i][0])])
    i += 1

df = pd.DataFrame(allStudents, columns=["studyhours", "gpa"])

labels = df.studyhours

# Establish the number of plots
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))

ax.set_title('Study Hours vs. GPA')
# You have to give your plot a name because it will be referenced in the motion_hover function
scatter = ax.scatter(df.studyhours, df.gpa, s=df.studyhours, c=df.gpa)

# Set titles and labels
ax.set_xlabel('Study Hours per Week')
ax.set_ylabel('GPA')

ax.set_xlim([0, 80])
ax.set_ylim([0, 4.5])

ax.set_axisbelow(True)
ax.grid(True, linestyle='--', alpha=0.6, zorder=0)

# Set up the basic plan of where the annotations go and how they look
annotation = ax.annotate(text='', xy=(0, 0), xytext=(15, 15), textcoords='offset points',
                          bbox={'boxstyle': 'round', 'fc': 'w'}, arrowprops={'arrowstyle': '->'})
annotation.set_visible(False)

# Assign the motion_hover function to the 'event' of moving the mouse over the plot
fig.canvas.mpl_connect('motion_notify_event', motion_hover)

# Fit a line and plot it
a, b = np.polyfit(df["studyhours"], df["gpa"], 1)
plt.plot(df["studyhours"], a * df["studyhours"] + b, color='red', label="Line of Best Fit")

# Add legend
plt.legend()

plt.show()
