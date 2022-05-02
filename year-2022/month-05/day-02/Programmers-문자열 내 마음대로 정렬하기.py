def solution(strings, n):
  dic = {}

  for word in strings:dic[word] = word[n]
  return list(dict(sorted(dict(sorted(dic.items())).items(), key = lambda item: item[1])).keys())