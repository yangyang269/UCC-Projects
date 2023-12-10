# Importing necessary modules
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def motion_hover(event):
    # We want to toggle the visibility so we need to know where we start
    is_visible = annotation.get_visible()

    # Checking if the mouse pointer is within the plot area
    if event.inaxes == ax:
        # Check if the mouse pointer is over a dot
        is_in, annotation_index = scatter.contains(event)
        if is_in:
            # Getting information about the dot
            data_point = scatter.get_offsets()[annotation_index['ind'][0]]
            annotation.xy = data_point

            # Formating the label text
            text_label = f'GPA: {data_point[1]}\nHours Studied per week: {data_point[0]}'

            # Showing the label as well as attaching the label to the dot
            annotation.set_text(text_label)
            annotation.set_visible(True)
            fig.canvas.draw_idle()
        else:
            # Turn off the label if you are not on a dot
            if is_visible:
                annotation.set_visible(False)
                fig.canvas.draw_idle()

# Loading data from csv files
with open("gpastudyhours2.csv", newline='') as studyhours2:
    reader = csv.reader(studyhours2)
    studyhours2 = list(reader)

with open("gpastudyhours3.csv", newline='') as studyhours3:
    reader = csv.reader(studyhours3)
    studyhours3 = list(reader)

with open("gpastudyhours4.csv", newline='') as studyhours4:
    reader = csv.reader(studyhours4)
    studyhours4 = list(reader)

# In studyhours3, the end grade is in percentage. Therefore I go through a process to convert the percentage to  a GPA
i = 1
while i < len(studyhours3):
    value = float(studyhours3[i][1])
    value = round(value / 100 * 4, 2)
    studyhours3[i][1] = value
    i += 1

# Creating one master list where values from all 3 csv files get combined into one list
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

# Using Pandas to create a datagrame, accessing the data in allStudents, and then creating two columns in the dataframe

df = pd.DataFrame(allStudents, columns=["studyhours", "gpa"])

# Establishing the number of plots, as well as stating the size of graphs
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8))

# Assinging a title to the graph
ax.set_title("Relationship between the amount of Study Hours per week and a student's GPA")
# This line of code actually generates the graph. It assigns the x and y axes (studyhours and gpa). It also determines the size and colour of the datapoints.
scatter = ax.scatter(df.studyhours, df.gpa, s=df.studyhours, c=df.gpa)

# Set titles and labels
ax.set_xlabel('Study Hours per Week')
ax.set_ylabel('GPA')

# Limiting the scales on the x and y axis
ax.set_xlim([0, 80])
ax.set_ylim([0, 4.5])

# Making sure that the grid generated is below the datapoints
ax.set_axisbelow(True)
# Creating the grid. Alpha determines the transparency of the grid lines, and linestyle determines the style of the grid lines.
ax.grid(True, linestyle='--', alpha=0.6, zorder=0)

# Set up the basic plan of where the annotations go and how they look
annotation = ax.annotate(text='', xy=(0, 0), xytext=(15, 15), textcoords='offset points',bbox={'boxstyle': 'round', 'fc': 'w'}, arrowprops={'arrowstyle': '->'})
annotation.set_visible(False)

# Assign the motion_hover function to the 'event' of moving the mouse over the plot
fig.canvas.mpl_connect('motion_notify_event', motion_hover)

# Finding a line of best fit and plotting it
# Since the line of best fit in this case is a linear line, the degree stated is 1
# Since the equation for a linear equation is y = ax + b, a and b are variables which get returned from the polyfit function
a, b = np.polyfit(df["studyhours"], df["gpa"], 1)
# Here the line actually gets plotted. You can see the ax + b equation, and the assignment of a colour and a label
plt.plot(df["studyhours"], a * df["studyhours"] + b, color='red', label="Line of Best Fit")

# Adding a legend for the trendline
plt.legend()

# Showing the graph
plt.show()
