from collections import OrderedDict

f = open("trace1", "r")
f_data = f.read()
f.close()
lines = f_data.split("\n")
sys_calls = []

for line in lines:
    sys_call = line.split("(")
    if(not(sys_call[0].startswith("+++")) and sys_call[0] != ""):
      sys_calls.append(sys_call[0])

syscalls=list(OrderedDict.fromkeys(sys_calls))
#print (syscalls)

o = open("output.svg", "w+")
o.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\r\n")
o.write("<svg width=\"400\" height=\"400\" xmlns=\"http://www.w3.org\" version=\"1.1\">\r\n")
r=0
degOffset=360/len(syscalls)
for syscall in syscalls:

  o.write("<text x=\"260\" y=\"200\" font-family=\"Verdana\" font-size=\"12\" transform=\"rotate(" +
          str(r*degOffset) + " 200,200)")
  if((r*degOffset)>90 and (r*degOffset) <= 270):
    o.write("rotate(180 260,200)\" text-anchor=\"end")
  o.write("\">" + syscall + "</text>\r\n")
  r+=1

o.write("</svg>\r\n")
o.close()

