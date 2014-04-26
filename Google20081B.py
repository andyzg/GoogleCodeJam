# INCOMPLETE

f = open("input.in")
output = open("output.out", "w")

class Person:
  def __init__(self, list=[]):
    self.numShake = list.pop(0)
    self.perf = [list[x:x+2] for x in xrange(0, len(list), 2)]
    
    for i in self.perf:
      s = str(i[0])
      if i[1] == 1:
        if s not in self.maltMap.keys():
          self.maltMap[s] = 1
        else:
          self.maltMap[s] += self.maltMap[s] + 1
      else:
        if s not in self.unmaltMap.keys():
          self.unmaltMap[s] = 1
        else:
          self.unmaltMap[s] = self.unmaltMap[s] + 1

def main():
  global shakeMap
  input = f.read().split("\n")
  numTest = int(input.pop(0))
  for i in range(0, numTest):
    milkshakes = int(input.pop(0))
    people = []
    for j in range(0, int(input.pop(0))):
      people.append(Person(map(int, input.pop(0).split(" "))))
    
    if milkshakes < len(people):
      output.write("Case #"+str(i+1)+": IMPOSSIBLE\n")
    else:
      for i in people:


main()
