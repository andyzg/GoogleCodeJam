import fileinput
import time
start_time = time.time()

input = open("input.in","r")
output = open("output.out", "w")
text = input.read().splitlines()
first = text.pop(0).split(" ")

L = int(first.pop(0))
D = int(first.pop(0))
N = int(first.pop(0))
words = []

for i in range(0, D):
  words.append(text.pop(0))
lol = 1
for i in text:
  x = []
  temp = ""
  tempBool = False
  for j in range(0, len(i)):
    if tempBool:
      if i[j] == ")":
        x.append(temp)
        temp = ""
        tempBool = False
      else:
        temp = temp + i[j]
    elif i[j] == "(":
      tempBool = True
    elif not i[j] == "(":
      x.append(i[j])
      
  count = 0

  good = True
  for word in words: 
    for index in range(0, L):
        if not word[index] in x[index]:
          good = False
          break
    if good:
      count += 1
    good = True
  output.write("Case #" + str(lol) + ": " + str(count)+"\n")
  lol += 1
print time.time() - start_time, "seconds"
