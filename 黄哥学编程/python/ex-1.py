"""
[1,[2]] = > [1,2]
[[1,2],[3,4]] => [1,2,3,4]
[1,2,[3,4,[5,6]]] => [1,2,3,4,5,6]
"""


def yiled_flat(lst):
  if(len(lst)) == 0:
    return []
  for item in lst:
    if isinstance(item, list):
      yield from yiled_flat(item)
    else:
      yield item


if __name__ == '__main__':
  arr = [1, [2, 3, [4, [5]]], [6, [7]], 8, 9, [10]]
  print(list(yiled_flat(arr)))
