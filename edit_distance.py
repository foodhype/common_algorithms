from sys import stdin


def edit_distance(a, b):
  dp = [[0 for _ in xrange(len(b) + 1)] for _ in xrange(len(a) + 1)]

  for i in xrange(1, len(a) + 1):
    dp[i][0] = i
  for j in xrange(1, len(b) + 1):
    dp[0][j] = j

  for i in xrange(1, len(a) + 1):
    for j in xrange(1, len(b) + 1):
      delete_min = dp[i - 1][j] + 1
      insert_min = dp[i][j - 1] + 1
      if a[i - 1] == b[j - 1]:
        replacement_min = dp[i - 1][j - 1]
      else:
        replacement_min = dp[i - 1][j - 1] + 1
      dp[i][j] = min(delete_min, insert_min, replacement_min)

  return dp[len(a)][len(b)]


def main():
  lines = stdin
  a = lines.next().rstrip()
  b = lines.next().rstrip()
  print edit_distance(a, b)

main()
