var Question = prompt('What do you want to find the Area of ?\n   triangle, square, rectangle, circle, parallelogram, trapezoid')
//console.log(Question)

function Triangle(){
    let b = prompt('What is b');
    let h = prompt('What is h');
    return('A = '+ .5 * b * h);
}

function Square(){
    let S = prompt('What is S');
    let S2 = Math.pow(S, 2)
    return ('A = ' + S2);
}

function Rectangle(){
    let L = prompt('What is L');
    let W = prompt('What is W');
    return ('A = ' + L * W);
}

function Circle(){
    let r = prompt('What is r');
    let Pow = Math.pow(r, 2);
    return ('A = ' + Pow,'π');
}

function Parallelogram(){
    let B = prompt('What is b');
    let H = prompt('What is h')
    return ('A = ' + B * H);
}

function Trapezoid(){
    let h = prompt('What is h')
    let b1 = prompt('What is base 1');
    let b2 = prompt('What is base 2');
    let B1 = b1 * 1
    let B2 = b2 * 1
    let BB = B1 + B2
    return ('A = '+ .5 * h * BB);
}

function Output(){
    if (Question == 'triangle'){
        return (Triangle())
    }
    if (Question == 'square'){
        return (Square())
    }
    if (Question == 'rectangle'){
        return (Rectangle())
    }
    if (Question == 'circle'){
        return (Circle())
    }
    if (Question == 'parallelogram'){
        return (Parallelogram())
    }
    if (Question == 'trapezoid'){
        return (Trapezoid())
    }
}


let output = Output();
var display = document.getElementById("area");
display.innerHTML = output.toString();