from collections import OrderedDict
from math import sin,cos
import sys
import re

class Node:
  def __init__(self, name):
    self.name = name
    self.edges = []
  def addEdge(self, node):
    self.edges.append(node)

inFile = None
outFile = None


if len(sys.argv) < 3:
  print("Not enough parameters\n" +
        "if=[file] input filename\n" +
        "of=[file] output file name\n\n")
  exit()

for i in range(len(sys.argv)):
  if(sys.argv[i].startswith("if")):
    inFile=sys.argv[i].replace("if=","")
  if(sys.argv[i].startswith("of")):
    outFile=sys.argv[i].replace("of=","")

if inFile is None or outFile is None:
  print("Missing parameter\n\n")
  exit()

f = open(inFile, "r")
f_data = f.read()
f.close()
lines = f_data.split("\n")
sys_calls = []
dep_sys_calls = []
dep_sys_calls_val = []
open_calls = []
parameters = []



i=0
for line in lines:
    sys_call_val = str(line[(line.rfind("="))+1:]).strip()
    sys_call = line.split("(")
    if(not(sys_call[0].startswith("+++")) and sys_call[0] != ""):
      sys_calls.append(sys_call[0])
      dep_sys_calls.append(sys_call_val + sys_call[0])
      dep_sys_calls_val.append(sys_call_val)
      param = re.search('\((.+?)\)', line)
      fd = re.search('\= (.+?)', line)
      if param:
          param_found = param.group(1)
      if fd:
          fd_found = fd.group(1)

      # if(sys_call[0] == 'open'):
      #     c = line[-1:]
      #     open_calls.append(c)


      i+=1

syscalls=list(OrderedDict.fromkeys(sys_calls))

#create circular SVG

o = open(outFile, "w+")
o.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\r\n")
o.write("<svg width=\"400\" height=\"400\" xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">\r\n")
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


###################END OF SVG SECTION

#create dependency graph




nodes = []

#to create a node:
# a = Node('a')
#to create a dependency:
# a.addEdge(b)  #a depends on b

#create nodes
for i in range(len(sys_calls)-1):
  nodes.append(Node(dep_sys_calls[i]))
  #if(sys_calls[i] = "read"):


#print nodes

#set dependencies



def dep_resolve(node, resolved, seen):
   print (node.name)
   seen.append(node)
   for edge in node.edges:
          if edge not in resolved:
                 if edge in seen:
                        raise Exception('Circular reference detected: %s -&gt; %s' % (node.name, edge.name))
                 dep_resolve(edge, resolved, seen)
   resolved.append(node)

resolved = []
dep_resolve(nodes[0], resolved, [])
for node in resolved:
   print (node.name)
