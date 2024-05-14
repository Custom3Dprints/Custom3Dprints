console.log("d = √(x2 - x1)2 + (y2 - y1)2")
let x1 = prompt('What is X1')
    console.log('x1 = '+x1)
let y1 = prompt('What is Y1')
    console.log('y1 = '+y1)
let x2 = prompt('What is X2')
    console.log('x2 = '+x2)
let y2 = prompt('What is Y2')
    console.log('y2 = '+y2)

let Step1 = (x2 - x1)
console.log('Step1 = '+Step1)
    let Step1Sq = (Math.pow(Step1, 2))    
    console.log('Step1sq = '+Step1Sq)
let Step2 = (y2 - y1)
console.log('Step2 = '+Step2)
    let Step2Sq = (Math.pow(Step2, 2))
    console.log('Step2sq = '+Step2Sq)
let Step3 = Step1Sq + Step2Sq
console.log('Step3 = '+Step3)
    
let d = Math.sqrt(Step3);
    //console.log(d);

let AnInteger = [0
    ,1,2,3,4,5,6,7,8,9,10,
    11,12,13,14,15,16,17,18,19,20,
    21,22,23,24,25,26,27,28,29,30,
    31,32,33,34,35,36,37,38,39,40,
    41,42,43,44,45,46,47,48,49,50,
    51,52,53,54,55,56,57,58,59,60,
    61,62,63,64,65,66,67,68,69,70,
    71,72,73,74,75,76,77,78,79,80,
    81,82,83,84,85,86,87,88,89,90,
    91,92,93,94,95,96,97,98,99,
    100,101,102,103,104,105,106,107,108,109,
    110,111,112,113,114,115,116,117,118,119,
    120,121,122,123,124,125,126,127,128,129,
    130,131,132,133,134,135,136,137,138,139,
    140,141,142,143,144,145,146,147,148,149,
    150,151,152,153,154,155,156,157,158,159,
    160,161,162,163,164,165,166,167,168,169,
    170,171,172,173,174,175,176,177,178,179,
    180,181,182,183,184,185,186,187,188,189,
    190,191,192,193,194,195,196,197,198,199,
                200];


let ans;
console.log('\nd = √('+ x2, x1 + ')2 + ('+ y2, y1+')2')
if (AnInteger.includes(d)){
    let d = Math.sqrt(Step3);
    ans = "Area = " + ('d = ',d)        // d = distance
}
else{
    var Rounded = d.toFixed(3)
    ans = "Area = " + ('d = √'+Step3)
}
let Decimal = prompt('Do you want it in decimal form? ').toLowerCase();
if (Decimal == 'yes' || Decimal == 'y'){
    ans = "Area = " + ('d = ',Rounded)
}

document.getElementById('area').innerHTML = ans;