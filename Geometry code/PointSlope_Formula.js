// Point slope = Y - y1 = m (x - x1)

var y1 = prompt("Enter y1: ")
var m = prompt('what is the slope');
var x1 = prompt('what is x1');

// Parse inputs as floats
m = parseFloat(m);
x1 = parseFloat(x1);
y1 = parseFloat(y1);



if (x1 > 0){
    document.getElementById('step2').innerHTML = 'Y - '+y1+' = '+m+" (X - "+x1+")";
    document.getElementById('step3').innerHTML = 'Y - '+y1+' = '+m+"x "+m*-x1;
}
else{
    document.getElementById('step2').innerHTML = 'Y - '+y1+' = '+m+" (X "+x1+")";
    document.getElementById('step3').innerHTML = 'Y - '+y1+' = '+m+"x + "+m*-x1;
}

// Calculate y-intercept
var yIntercept = m * -x1 + y1;
// Output the equation in slope-intercept form

if(y1>0){
    document.getElementById('step4').innerHTML = 'Y = ' + m + 'x + ' + yIntercept;
}
else{
    document.getElementById('step4').innerHTML = 'Y = ' + m + 'x - ' + yIntercept;
}
