import operator
import sys

f = open("input.in", "r")
output = open("output.out", "w")

def getMinScalar(v1, v2):
  v1.sort()
  v2.sort(reverse=True)
  return sum(map(operator.mul, v1, v2))

def main():
  input = f.read().split("\n")
  numTest = int(input.pop(0))

  for i in range(0, int(numTest)):
    length = int(input.pop(0))
    v1 = map(int, input.pop(0).split(" "))
    v2 = map(int, input.pop(0).split(" "))
    output.write("Case #"+str(i+1)+": "+str(getMinScalar(v1, v2))+"\n")
main()
