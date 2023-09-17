  const myFunction = async () => {
      let text = document.getElementById('password').innerHTML;
      await navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
  }

    function change_text(){
    document.getElementById("nocopy").innerHTML = "PASSWORD COPIED";
}

function functionGetter() {
                       myFunction();
                        change_text();
}
var slider = document.getElementById("mySlider");
var output = document.getElementById("value");
output.innerHTML = slider.value;
slider.oninput = function() {
  output.innerHTML = this.value;
  if(document.getElementById('numberscheck').checked){
    localStorage.setItem('sex', 'male');
}
}
