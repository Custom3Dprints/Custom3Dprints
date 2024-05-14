var Question = prompt('              What are you trying to find the volume of?'+'\n'+ 'rectangular prisim, other prisims, cylinder, pyrimid, cone, sphere, hemishpere').toLowerCase();

let formula;
let ans;

if (Question == 'rectangular prisim'){
    let l = prompt('what is the length')
    let w = prompt('what is the width')
    let h = prompt('what is the height')
    console.log('\n' + 'V = '+ l * w * h)
    formula = 'V = l * w * h';
    ans = "V = "+l*w*h;
}if (Question == 'other prisim'){
    let b = prompt('what is b')
    let h = prompt('what is h')
    let B = .5 * b * h
    let V = B * h
    console.log(V)
    formula = 'V = 1/2 * b * 2h';
    ans = "V = "+V;
}if (Question == 'cylinder'){
    let r = prompt('what is r')
    let Pi = Math.pow(r, 2)
    let st1 = Pi
    let h = prompt('what is the height')
    let V = st1 * h
    console.log('V = '+ V + 'π')
    formula = "V = πr²h";
    ans = 'V = '+ V + 'π'
}if (Question == 'pyrimid'){
    let l = prompt('what is the length')
    let w = prompt('what is the width')
    let B = l * w
    let h = prompt('what is the height')
    let num = B * h
    let V = num / 3
    console.log('V = '+V)
    formula = "V = (l * w * h) / 3";
    ans = 'V = ' + V;
}if (Question == 'cone'){
    let l = prompt('what is the length')
    let r = prompt('what is r')
    let h = prompt('what is the height')
    let sq = Math.pow(r, 2)
    let numerator = l * sq * h / 3
    let answer = numerator + 'π'
    console.log('V = '+answer)
    formula = "V = (l * r² * h)/3 π";
    ans = 'V = '+ answer;
}if (Question == 'sphere'){
    let r = prompt('what is r')
    let cubed = Math.pow(r, 3)
    let numerator = 4 * cubed
    let product = numerator / 3
    let answer = product + ' π'
    console.log(answer)
    formula = "V = (r³ * 4)/3 π";
    ans = 'V = '+ answer;
}if (Question == 'hemisphere'){
    let r = prompt('what is r')
    let cubed = Math.pow(r, 3)
    let answer = cubed + '  *  4/3 ' + ' *  π'+'\n'+'      2'
    console.log(answer)
    formula = "V = 2/3πr³";
    ans = 'V = '+ ((2/3) * cubed )+ 'π';
}

document.getElementById('formula').innerHTML = formula;
document.getElementById('ans').innerHTML = ans;
