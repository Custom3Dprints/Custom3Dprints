var string = "hello world"

//console.log(string[0]);
//console.log(string[string.length - 1])

//document.getElementById("someText").innerHTML = "hey there";
//var age = prompt("what is your age? ");
//document.getElementById("someText").innerHTML = "hey there "+age;

///////////////////////////////////////////////////////////////////

//Numbers //

var num1 = 23;// int
var num2 = 2.3;// float
//console.log(5+10); //add
//console.log(10-5); //subtract
//console.log(5*10); //multiply
//console.log(10/2); //divide
//console.log(10%3); //remainder
num1 ++; //increment by 1
num1 --; //decrement by 1
num1 += 10 //increment by 10 
num1 -= 10 //decrement by 10

///////////////////////////////////////////////////////////////////

//Functions //

var rnum = Math.floor(Math.random() * 101)

function getGuess(first, last){
    var user_guess = Number(prompt("Enter you best guess(1-100): "))
    if (user_guess >= first && user_guess <= last){
        return user_guess;
    }else {
        while (true){
            var user_guess = Number(prompt("Enter you best guess(1-100): "))
            if (user_guess >= first && user_guess <= last){
                return user_guess;
            }
        }
        
    }
}
function guessWin(number, guess){
    if (guess == number){
        text = "Congradulations ... You guessed the Mistery Number!"
        console.log(text)
        //document.getElementById("text").innerHTML = text
        return true
    }if (guess > number){
        text = guess+" is too High"
        console.log(text)
        //document.getElementById("text").innerHTML = text
        return false
    }if (guess < number){
        text = guess+" is too Low"
        console.log(text)
        //document.getElementById("text").innerHTML = text
        return false
    }
}
function game(){
    for (let i = 1; i <= 7; i++){
        var round = (("Round "+i+" of 7 ")+("-"*35))
        document.getElementById("round").innerHTML = round
        var guess = getGuess(1, 100)
        var guesswin = guessWin(rnum, guess)
        if (guesswin == true){
            break
        }
    }
    
}
function output(){
    game()
    
    while (true){
        var try_again = prompt("Do you want to try again(y/n)? ")
        if (try_again == "y"){
            game()
        }
        break
    }
}
//output()

/////////////////////////////////////////////////////////////////////////

// Data Types

let name = {first: "marjorie", last: "middlesteadt"}; //object

let fruit = "Mango"
let fruits = "Mango, apple, banana"

console.log(fruit.length); //length
console.log(fruit.indexOf("an")); //index num of first char
console.log(fruit.slice(2, 4)); //inclusive, noninclusive
console.log(fruit.replace("m", "2")); // replace
console.log(fruit.toUpperCase()); //all uppercase
console.log(fruit.toLowerCase()); //all lowercase
console.log(fruit[2]); //what char is at the index
console.log(fruit.split("")); //splits at the char
console.log(fruits.split(",")); //splits at the char

/////////////////////////////////////////////////////////////////////////

// Array aka. List
let food = ['Mango', ' apple', ' banana'];
food = new Array('banana', 'mango', 'apple')
console.log(food[1]) //mango

