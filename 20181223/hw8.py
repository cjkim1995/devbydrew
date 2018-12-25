def frequencySort(s):
  """
  Given a string, sort it in decreasing order based on the frequency of characters.
  
  Input: "tree"
  Output: "eert"

  Input:"Aabb"
  Output: "bbaA" or "bbAa"
  """

  assert isinstance(s, str), "Not a string!" #check type for string
  # counts = dict()
  # for i in s:
  #   if i not in counts:
  #     counts[i] = 1
  #   else:
  #     counts[i] += 1
  # ordered_list = []
  # for key in sorted(counts.iteritems(), key = lambda (k, v): v, k):
  #   ordered_list.append(key)
  # for j in ordered_list:

  string_set = set(s)
  ordered_list = []
  for i in string_set:
    ordered_list.append((i, s.count(i)))
  ordered_list.sort(key = lambda letter: letter[1], reverse = True)

  string_to_print = ''
  for item in ordered_list:
    string_to_print += item[0] * item[1]

  return string_to_print