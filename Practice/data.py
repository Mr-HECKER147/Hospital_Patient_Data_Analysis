import csv
import random
import datetime


def generate_data(filename='data.csv', rows=20):
    headers = ['id', 'name', 'age', 'score', 'date']
    names = ['Alice', 'Bob', 'Carol', 'David', 'Eva', 'Frank', 'Grace', 'Hugo','Haytham','Connor','Edward','Desmond','Ezio']
    start = datetime.date.today()

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for i in range(1, rows + 1):
            name = random.choice(names)
            age = random.randint(18, 65)
            score = round(random.uniform(0, 100), 2)
            date = (start + datetime.timedelta(days=random.randint(0, 365))).isoformat()
            writer.writerow([i, name, age, score, date])


if __name__ == '__main__':
    generate_data('data.csv', 50)

# # Plotting Functions
# plt.plot()          # Line plot 
# plt.scatter()       # Scatter plot
# plt.bar()           # Bar chart
# plt.barh()          # Horizontal bar chart
# plt.hist()          # Histogram
# plt.box()           # Box plot
# plt.pie()           # Pie chart
# plt.stem()          # Stem plot
# plt.step()          # Step plot
# plt.fill()          # Filled area plot
# plt.imshow()        # Image display
# plt.contour()       # Contour plot
# plt.quiver()        # Vector field plot

# # Figure and Axes
# plt.figure()        # Create a new figure
# plt.subplot()       # Add subplot
# plt.subplots()      # Create multiple subplots
# plt.axes()          # Create axes

# # Customization
# plt.title()         # Add title
# plt.xlabel()        # Label x-axis
# plt.ylabel()        # Label y-axis
# plt.legend()        # Add legend
# plt.grid()          # Add grid
# plt.xlim()          # Set x-axis limits
# plt.ylim()          # Set y-axis limits
# plt.xticks()        # Set x-axis ticks
# plt.yticks()        # Set y-axis ticks
# plt.text()          # Add text annotation
# plt.annotate()      # Annotate plot
# plt.colorbar()      # Add colorbar

# # Display and Saving
# plt.show()          # Display plot
# plt.savefig()       # Save figure to file
# plt.close()         # Close figure

# # Common Keywords
# # marker              - Point marker style ('o', 's', '^', etc.)
# # linestyle           - Line style ('-', '--', '-.', ':')
# # linewidth           - Line width
# # color               - Color of plot elements
# # alpha               - Transparency (0-1)
# # label               - Legend label
# # kind                - Plot type (for df.plot())
# # figsize             - Figure size as (width, height)