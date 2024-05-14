var x1 = prompt('Enter x1: ')
var y1 = prompt('Enter y1: ')
var x2 = prompt('Enter x2: ')
var y2 = prompt('Enter y2: ')
var X = (x1 * 1)
var X2 = (1 * x2)
var Total = (X + X2);
//console.log('Total = '+Total)



var Y = (y1 * 1)
var Y2 = (1 * y2)
var Total_1 = (Y + Y2);
//console.log('Total_1 = '+Total_1)
let Denominator = 2

//formula
let step1 = ('('+x1+' + '+ x2+') / 2' +'   ,   ('+ y1+' + '+ y2+') / 2')

//answer
let step2 = (Total + ' / 2,' + Total_1 + ' / 2');

let step3 = ('↑'+'  Simplify'+' ↑'+ '\n')

let step4 = ('Format:  M = (A, B)')

document.getElementById('step1').innerHTML = step1;
document.getElementById('step2').innerHTML = step2;
document.getElementById('step3').innerHTML = step3;
document.getElementById('step4').innerHTML = step4;