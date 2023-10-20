/*
REPL use Developer console, Nodejs
File execution with script tag and/or Nodejs

Script tag !!Concurrency is important!!
Typically in head with attribute but the key ones are

async- continue parsing HTML while you load the file
defer- Wait until HTML is parsed to run this code


const is a read only variable
let is a read-write variable
Weird variables
var is function scoped but most of the time just use let
We can give no data type but it will end up causing a bug

we have c based flows
if else, for loops, while, case, functions
for of(list-iteration)
for in(object/dictionary iteration)
do while(variant of while loop)




*/
function rng(){
    
    const ranNum = Math.floor(Math.random()*100)+1
    let guess;
    do{
        guess=prompt("guess?");
        if(guess<ranNum){
            alert("low")
        }
        else if (guess>ranNum){
            alert("too high")
        }
        }while(guess!=ranNum);
        alert("its lit");

    }

/*
Data types
special erros null which points to nothing and undefined which has no value
boolean
number
bigint
strings
array which is basically a list
object


Type conversion in javascript is intense
typeof operator can be used to find what operator we have

Truthy/Falsy
Truthy
non-zero, non-empty strings, all objects and arrays
Falsy
Zero, Empty string NaN, undefined, null

== and != allow type conversion
=== and !== do not allow type conversion

variables can be functions
cannot call a function when passing a variable if it has no return value
*/