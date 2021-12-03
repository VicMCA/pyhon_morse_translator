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

def morse_to_text(codigo):
  '''
  Realiza a tradução do input recebido, de código-morse para ASCII em maiúsculas.
  Pontuação e acentos não inclusos.
  '''
  caracteres_aceitos = ['.', '-', '/']
  caractere = ''
  lista_caracteres = []
  caractere_anterior = ''

  for char in codigo:
    if char not in caracteres_aceitos:
      return "O código enviado possui caracteres não-aceitos."
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
          pass
        caractere = ''
      caractere_anterior = x
    
    return ''.join(lista_caracteres)


if __name__ == "__main__":
  print(morse_to_text('--/---/.-./..././/-.-./---/-../.' + '/'))