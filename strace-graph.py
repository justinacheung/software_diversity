from graphics import *
import matplotlib.pyplot as plt

#
x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [7,8,2,4,2]

plt.bar(x, y, label = 'Bar1', color = 'teal')
plt.bar(x2, y2, label = 'Bar2', color = 'blue')

# #Plots the values
# plt.plot(x, y, label = 'First Line') #label = adds this to a legend
# plt.plot(x2, y2, label = 'Second Line')

#Graph Labels/Titles
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Software Diversity\nSTRACE Calls')

#Adds legend to graph
plt.legend()

#Shows the graph
plt.show()
