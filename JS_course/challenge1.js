//ChALLANGE 1: Your Age in Days
function ageInDays(){
    var birthyear = prompt("What year were you born? ");
    var inDays = (2022 - birthyear) * 365;
    var h1 = document.createElement('h1') //creates h1 tag
    var id = document.createTextNode('You are '+ inDays+' days old.') //text in h1 tag
    h1.setAttribute('id', 'ageInDays') //add the id in the h1 tag => <h1 id="startbutton"></h1>
    h1.appendChild(id) // appends id to the h1 tag
    document.getElementById('flex-box-result').appendChild(h1) //displays on the html doc
}

function reset(){
    document.getElementById('ageInDays').remove();
}