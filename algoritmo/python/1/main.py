def sum_divisors(n):
  i, sum = 1, 0
  if n == 0:
      return sum
  # Return the sum of all divisors of n, not including n
  while(i < n):
      if(n%i == 0):
          sum = sum + i
      i = i + 1
  return sum

print(sum_divisors(0))
print(sum_divisors(1))
print(sum_divisors(36))
print(sum_divisors(102))