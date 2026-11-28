def get_longest(*num):
  if len(num) == 0:
    return None

  max_len_str = num[0]
  for n in num:
    if len(n) > len(max_len_str):
      max_len_str = n
  return max_len_str
print(get_longest("ShreeGholap", "Payal", "Zaria", "Yogesh"))