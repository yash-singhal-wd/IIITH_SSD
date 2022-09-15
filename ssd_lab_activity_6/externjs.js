
function KeyPress(e) {
    var evtobj = window.event? event : e
    if (evtobj.keyCode == 77 && evtobj.ctrlKey) this.onclick=myFunction(); ;
}document.onkeydown = KeyPress;

function checkUppercase(str){
    for (var i=0; i<str.length; i++){
      if (str.charAt(i) == str.charAt(i).toUpperCase() && str.charAt(i).match(/[a-z]/i)){
        return true;
      }
    }
    return false;
};
function hasNumber(str) {
  return /\d/.test(str);
}

function passcheck()
{
    let in1=document.getElementById("s_pass").value;
    let in2=document.getElementById("cs_pass").value;
    // alert(in1+" "+ in2);
    if(in1==in2)
    {
        return 1;
    }
    else
    {
        alert("The passwords should be same");
        return 0;
    }
}

function myFunction(event) {
  var x = event.target.value;

  if( !checkUppercase(x) && !hasNumber(x) ){
    var hello = document.getElementById("s_con");
    hello.createTextNode('Invalid Name');
  } else {
    console.log("here_now");
    var msg = '';
    var ele = document.getElementById("s_name").innerHTML;
    var newVar = ele + msg;
    document.getElementById("s_name").innerHTML = newVar;
  }
//   document.getElementById("demo").innerHTML = "The pressed key was: " + x;
}

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev){
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}

function myFunction() {
   var element = document.body;
   element.classList.toggle("dark-mode");
}