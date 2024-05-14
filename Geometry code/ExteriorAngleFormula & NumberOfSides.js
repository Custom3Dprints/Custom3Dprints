let Question = prompt('what do you want to know? Exterior Angle or Number of Sides or Both')

let formula;
let formula2;
let ans;
let ans2;

if (Question.toLowerCase() =='exterior angle'){
    formula = ('Exterior Angle Formula => 360'+'\n            ', '             n')
    let n = prompt('What is n')
    let result = 360/n
    ans = ('Exterior Angle = '+result)
    document.getElementById('formula').innerHTML = formula;
    document.getElementById('output').innerHTML = ans;
    
}
else if (Question.toLowerCase() == 'number of sides'){
    formula = ('\n'+'Number of Sides Formula:'+ '\n             '+ '              n = 360' + '\n        '
    ,'              Exterior Angle')
    let n = prompt('What is n')
    let result = 360/n
    let answer = 360 / result
    ans = ('Number of Sides = '+answer)
    document.getElementById('formula').innerHTML = formula;
    document.getElementById('output').innerHTML = ans;
    
}
else if (Question.toLowerCase() == 'both'){
    console.log('Exterior Angle Formula => 360'+'\n            ', '             n')
    let n = prompt('What is n')
    let result = 360/n
    ans = ('Exterior Angle = '+result)
    
    console.log('  ')
    
    formula2 = ('\n'+'Number of Sides Formula:'+ '\n             '+ '              n = 360' + '\n        '
    ,'              Exterior Angle')
    let answer = 360 / result
    ans2 = ('Number of Sides = '+answer)
    


    document.getElementById('formula').innerHTML = 'Exterior Angle Formula => 360/n';
    document.getElementById('output').innerHTML = ans;

    var newdiv = document.createElement("div");
    newdiv.id = "formula2";
    document.body.appendChild(newdiv);

    document.getElementById("formula2").innerHTML = '\nNumber of Sides Formula:\n                           n = 360\n                      Exterior Angle';
    

    var newdiv2 = document.createElement("div");
    newdiv2.id = "ans2";
    document.body.appendChild(newdiv2);

    document.getElementById("ans2").innerHTML = ans2;
}



