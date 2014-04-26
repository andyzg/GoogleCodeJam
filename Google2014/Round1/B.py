# Incomplete
def main(input, cases):
  o = open("output.out", "w")
  for i in range(cases):
    case = int(input.readline())
    data = dict()
    for j in range(case-1):
      pair = read(input) 
      add(pair, data)
      add([pair[1], pair[0]], data)

    output = solve(data)
    o.write("Case #{num}: {ans}\n".format(num=str(1+i), ans=output))

def add(pair, data): 
  if not pair[0] in data:
    data[pair[0]] = [pair[0]]
  else:
    data[pair[0]].append(pair[1])

def solve(data):
  minimum = 9999999999
  for i in data:
    for j in data[i]:
      remove = solve(data, j, i)
      if remove < minimum:
        minimum = remove 
  return minimum

def solve(data, num, prev):
  length = len(data) 
  
def read(input):
  return input.readline().rstrip('\n').split(" ")
if __name__ == "__main__":
  file = open("input.in", "r")
  cases = int(file.readline())
  main(file, cases)
