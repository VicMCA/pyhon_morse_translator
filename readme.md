# Desafio: Tradutor de Código Morse

Este é um tradutor de código morse para alfabeto. Reconhece todas as 26 letras do alfabeto mais os algarismos de '0' à '9'. Os inputs reconhecidos são:  

<pre>
`.`  para 'dots'  
`-`  para 'dashes'  
`/`  para delimitação de caracteres  
`//` para espaço entre palavras  
</pre>

Acentuações, pontuações e caracteres especiais não são reconhecidos. Todos os caracteres serão retornados como maiúscula quando aplicável.  

Etapas a serem realizadas:  
1. Tratamento de erros para inputs inválidos
2. Tornar o programa acessível através de uma API
3. Conectar a API à um frontend básico
<br/><br/>
  
## Definição do desafio:
Precisamos que você crie um repositório no github ou gitlab e depois inicie um projeto que tenha o objetivo de criar uma tradução de código morse. A ideia é uma solução baseada em socket que recebe um código morse e converte ele em texto. Imagine que o cliente vai enviar "." e "-" e o servidor vai receber estas informações e interpretar o que aquele código morse representa. 

Não é necessário você se preocupar com gramática, concordância, frases complexas, este não é o objetivo do desafio. 

O objetivo do desafio é você definir uma arquitetura que resolva a solução utilizando o código morse como protocolo de comunicação e pensando em como esta solução poderia ser criada de forma que fosse o mais escalável possível.

Reflita sobre a arquitetura que você gostaria de usar, que serviços teria e como eles iriam se comunicar. Se você achar interessante usar RabbitMQ, Celery, Redis ou qualquer outra tecnologia similar, sinta-se à vontade para fazer. Se você preferir usar só Python com Django ou Flask, também é possível. Você é livre para criar a arquitetura que você achar mais interessante.

É importante para a gente você descrever o que motivou suas decisões e caso você tivesse mais tempo como seria a evolução desta arquitetura/produto.
<br/><br/>

## Morse cheat sheet:

```
A = .-      B = -...    C = -.-.    D = -..     E = .       F = ..-.
G = --.     H = ....    I = ..      J = .---    K = -.-     L = .-..
M = --      N = -.      O = ---     P = .--.    Q = --.-    R = .-.
S = ...     T = -       U = ..-     V = ...-    W = .--     X = -..-
Y = -.--    Z = --..

0 = -----   1 = .----   2 = ..---   3 = ...--   4 = ....-   5 = .....
6 = -....   7 = --...   8 = ---..   9 = ----.
```

### Exemplo
MORSE CODE = `--/---/.-./..././/-.-./---/-../.`