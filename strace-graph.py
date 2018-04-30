from collections import OrderedDict
from math import sin,cos

f = open("trace1", "r")
f_data = f.read()
f.close()
lines = f_data.split("\n")
sys_calls = []

i=0
for line in lines:
    sys_call = line.split("(")
    if(not(sys_call[0].startswith("+++")) and sys_call[0] != ""):
      sys_calls.append(sys_call[0])
      i+=1

syscalls=list(OrderedDict.fromkeys(sys_calls))
#print (syscalls)

o = open("output.svg", "w+")
o.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\r\n")
o.write("<svg width=\"400\" height=\"400\" xmlns=\"http://www.w3.org\" version=\"1.1\">\r\n")
radius=60
angle=0
cx=200
cy=200
r=0
degOffset=360/len(syscalls)
for syscall in syscalls:

  o.write("<text x=\""+str(cx+radius)+"\" y=\""+str(cy)+"\" font-family=\"Verdana\" font-size=\"12\"" +
          " transform=\"rotate(" +
          str(r*degOffset) + " "+str(cx)+","+str(cy)+")")
  if((r*degOffset)>90 and (r*degOffset) <= 270):
    o.write("rotate(180 "+str(cx+radius)+","+str(cy)+")\" text-anchor=\"end")
  o.write("\">" + syscall + "</text>\r\n")
  r+=1

for j in range(i-1):
  o.write("<line " +
          "x1=\"" + str(cx + radius * cos(syscalls.index(sys_calls[j]) * degOffset)) + "\" " +
          "y1=\"" + str(cy + radius * sin(syscalls.index(sys_calls[j]) * degOffset)) + "\" " +
          "x2=\"" + str(cx + radius * cos(syscalls.index(sys_calls[j+1]) * degOffset)) + "\" " +
          "y2=\"" + str(cy + radius * sin(syscalls.index(sys_calls[j+1]) * degOffset)) + "\" " +
          "style=\"stroke:rgb(0,0,0);stroke-width:1\" />")

o.write("</svg>\r\n")
o.close()

