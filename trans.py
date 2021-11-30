def trans():
  table = {
    'aaa': 'u',
    'eee': 'o',
    'iii': 'i',
    'ooo': 'e',
    'uuu': 'a'
  }

  string = 'aaaeeeiiiooouuu'
  traducao = string.maketrans(table)

  print(string)
  print(string.translate(traducao))

trans()