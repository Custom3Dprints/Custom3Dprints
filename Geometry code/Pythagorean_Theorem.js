let find = prompt('What are you trying to find? A, B or C');

if (find.toLowerCase() == 'a'){

    let B2 = prompt('What is B ')
    let C2 = prompt('What is C ')

    let step2 = C2**2 - B2**2;
    document.getElementById('step1').innerHTML = 'a² + '+ B2**2 + ' = ' + C2**2;
    document.getElementById('step2').innerHTML = 'a² ' + ' = ' + step2;
    document.getElementById('step3').innerHTML = 'a ' + ' = √' + step2;
}
else if (find.toLowerCase() == 'b'){

    let A2 = prompt('What is A ')
    let C2 = prompt('What is C ')

    let step2 = C2**2 - A2**2;
    document.getElementById('step1').innerHTML = A2**2 +' + b² = ' + C2**2;
    document.getElementById('step2').innerHTML = 'b² ' + ' = ' + step2;
    document.getElementById('step3').innerHTML = 'b ' + ' = √' + step2;
}
else if (find.toLowerCase() == 'c'){

    let A2 = prompt('What is A ')
    let B2 = prompt('What is B ')

    let step2 = A2**2 + B2**2;
    document.getElementById('step1').innerHTML = A2**2 + "+" + B2**2 + " = C²";
    document.getElementById('step2').innerHTML = 'C² ' + ' = ' + step2;
    document.getElementById('step3').innerHTML = 'C ' + ' = √' + step2;
}