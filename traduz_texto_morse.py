tabela_char_to_morse = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
  'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
  'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
  '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
  '7': '--...', '8': '---..', '9': '----.', '/': '/', ' ': ''
}

def text_to_morse(codigo):
  '''
  Realiza a tradução do input recebido, de texto para código morse.
  Pontuação e acentos não inclusos.
  '''
  caracteres_aceitos = tabela_char_to_morse.keys()
  lista_caracteres = []

  def separar(string):
    return '/'.join(string) + '/' 
    pass

  codigo = separar(codigo)

  for char in codigo:
    if char not in caracteres_aceitos:
      return "O código enviado possui caracteres não-aceitos."
  else:
    for x in codigo:
      lista_caracteres.append(tabela_char_to_morse[f'{x}'])
    return ''.join(lista_caracteres[0:-1])


if __name__ == "__main__":
  print(text_to_morse('MORSE CODE'))