<<<<<<< HEAD
from graphics import *
import matplotlib.pyplot as plt
import svgwrite

f = open("trace1", "r")
f_data = f.read()
lines = f_data.split("\n")
i = 0
sys_calls = []

for line in lines:
    sys_call = line.split("(")
    sys_calls.append(sys_call[0])
    i += 1

print (sys_calls)

dwg = svgwrite.Drawing('test.svg', profile = 'tiny')
dwg.add(dwg.line((0,0), (10,0), stroke = svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 0.2), fill = 'red'))
dwg.save()

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

#Graph Labels/Titles.
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Software Diversity\nSTRACE Calls')

#Adds legend to graph
plt.legend()

#Shows the graph
plt.show()
=======
from graphics import *
import matplotlib.pyplot as plt

#
x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [7,8,2,4,2]

#Displays a bar graph
plt.bar(x, y, label = 'Bar1', color = 'teal')
plt.bar(x2, y2, label = 'Bar2', color = 'blue')

# #Plots the values
# plt.plot(x, y, label = 'First Line') #label = adds this to a legend
# plt.plot(x2, y2, label = 'Second Line')

#Graph Labels/Titles.
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Software Diversity\nSTRACE Calls')

#Adds legend to graph
plt.legend()

#Shows the graph
plt.show()
>>>>>>> 717df77dd83c30fa208a088361543bfe02148b33
