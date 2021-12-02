'''
Morse cheat sheet:

Símbolos usados:
.  Dot
-  Dash
/  Space between characters
// Space between words

A = .-      B = -...    C = -.-.    D = -..     E = .       F = ..-.
G = --.     H = ....    I = ..      J = .---    K = -.-     L = .-..
M = --      N = -.      O = ---     P = .--.    Q = --.-    R = .-.
S = ...     T = -       U = ..-     V = ...-    W = .--     X = -..-
Y = -.--    Z = --..

0 = -----   1 = .----   2 = ..---   3 = ...--   4 = ....-   5 = .....
6 = -....   7 = --...   8 = ---..   9 = ----.

MORSE CODE = 
--/---/.-./..././/-.-./---/-../.
'''

def morse():
  '''
  Contém o dicionário e realiza a tradução do input 
  recebido, de código-morse para ASCII em maiúsculas.
  
  Pontuação e acentos não inclusos.
  '''
  tabela_morse_to_char = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', 
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', 
    '--...': '7', '---..': '8', '----.': '9', 'c': '', 'space': ' ',
  }

  tabela_char_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.', 'c': '', 'space': ' ',
  }
  
  # codigo = (input('Insira abaixo o código morse:\n> ') + '/')
  codigo = '--/---/.-./..././/-.-./---/-.././'

  caracteres_aceitos = ['.', '-', '/']
  caractere = ''
  lista_caracteres = []
  caractere_anterior = ''

  for char in codigo:
    if char not in caracteres_aceitos:
      # return "O código enviado possui caracteres não-aceitos."
      print("O código enviado possui caracteres não-aceitos.")
      break
  else:
    for x in codigo:
      if x == '.' or x == '-':
        caractere += x
      elif x == '/':
        if caractere != '':
          lista_caracteres.append(tabela_morse_to_char[f'{caractere}'])
        if caractere_anterior == '/':
          lista_caracteres.append(' ')
        else:
          # lista_caracteres.append('')
          pass
        caractere = ''
      caractere_anterior = x
    # return ''.join(lista_caracteres)
    print(''.join(lista_caracteres))


if __name__ == '__main__':
    morse()