def main(input, cases):
  for i in range(cases):
    output = solve()
    print("Case #{num}: {ans}".format(num=str(i+1), ans=output))

if __name__ == "__main__":
  file = open("input.in", "r")
  cases = int(file.readline())
  main(file, cases)
