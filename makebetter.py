"""Script I wrote for adding a right brace to each end of tag in a CSS File.
The CSS File was written in a single line. This Script basically makes the whole thing more readable."""


f = open ("initial.txt",'r')

contents = f.read()

c = []

for char in contents:
      c.append(char)
      
count =0      
for t in c:
    count+=1
    if t == "}":
        c.insert(count,"\n")
    else:
        pass
        
newcontents = ''.join(c)        
f2 = open("output.css",'w')
f2.write(newcontents)

                             
