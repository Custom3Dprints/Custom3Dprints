// Point slope = Y - y1 = m (x - x1)

var y1 = prompt("Enter y1: ")
var m = prompt('what is the slope');
var x1 = prompt('what is x1');

// Parse inputs as floats
m = parseFloat(m);
x1 = parseFloat(x1);
y1 = parseFloat(y1);



if (x1 < 0){
    num = m * -x1 - y1;
    document.getElementById('step2').innerHTML = 'Y - '+y1+' = '+m+" (X "+x1+")";
    document.getElementById('step3').innerHTML = 'Y - '+y1+' = '+m+"x + "+m*-x1;
    document.getElementById('step4').innerHTML = 'Y = ' + m + 'x + ' + num;
}
else if(y1 < 0){
    num = m * -x1 - y1;
    document.getElementById('step2').innerHTML = 'Y '+y1+' = '+m+" (X - "+x1+")";
    document.getElementById('step3').innerHTML = 'Y '+y1+' = '+m+"x - "+m*+x1;
    document.getElementById('step4').innerHTML = 'Y = ' + m + 'x + ' + num;
}
else if(x1>0 && y1>0){
    num = y1 + (m*-x1);
    document.getElementById('step2').innerHTML = 'Y - '+y1+' = '+m+" (X - "+x1+")";
    document.getElementById('step3').innerHTML = 'Y - '+y1+' = '+m+"x + "+m*-x1;
    document.getElementById('step4').innerHTML = 'Y = ' + m + 'x + ' + num;
}

