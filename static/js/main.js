function limparResultado() {
  let texto = document.getElementById("resultado-texto");
  texto.innerHTML = '<br/>';
}

function removerCaracteres() {
  let campoCodigo = document.getElementById("codigo");
  let codigo = campoCodigo.value;
  let char = codigo[(codigo.length-1)];

  if (char != '.' && char != '-' && char != '/' && char != (undefined || null)) {
    codigoCorrigido = codigo.slice(0, codigo.length -1);
    campoCodigo.value = codigoCorrigido;
  }
}