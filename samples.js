/* SAMPLES
string.splice(0, string.length - 1);

<button onclick="removeCharacter()">
  Remove Character
</button>


function removeCharacter() {
  originalString = 'GeeksForGeeks';
  firstCharRemoved = originalString.slice(1);
  lastCharRemoved = 
    originalString.slice(0, originalString.length - 1);
  document.querySelector('.output1').textContent
          = firstCharRemoved;
  document.querySelector('.output2').textContent
          = lastCharRemoved;
}

<form id="newForm">
   Student Name<br><input type="text" name="sname"><br>
   Student Subject<br><input type="password" name="subject"><br>
   <input type="button" onclick="newFunction()" value="Reset">
</form>

function newFunction() {
  document.getElementById("newForm").reset();
}
*/  