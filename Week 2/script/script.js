let a = 5;
let b = 'BenYehuda';
let c = 'Israel';
console.log(a, b, c)
let globalAddress = "I live in" + " " + a + " " + b + " "
 + "in" + " " + c
console.log(globalAddress)

let x = 2003;
let y = 2023;
let z = y - x;
console.log(z)
let year = "I wil be" + " "+ z + " " + "in" + " " + y
console.log(year)

let pets = ["cat", "dog", "fish", "rabbit", "cow"]
console.log(pets[1])
pets.splice(3,1, "horse")
console.log(pets)
console.log(pets.length)

let isBoss = confirm("Are you the boss?");
alert(isBoss);

let age = prompt('How old are you?', 20);
alert(`You are ${age} years old!`); 

let colors = ["blue", "yellow", "green" ]; 
colors.push("orange") 
console.log(colors)

let colors1 = ["blue", "yellow", "green" ]; 
colors1.pop() 
console.log(colors1) 

let colors2 = ["blue", "yellow", "green" ]; 
colors2.splice(1, 1, 45, 23); 
console.log(colors2)

let colors3 = ["blue", "yellow", "green", "pink" ]; 
let favorite = colors3.slice(2) 
console.log(favorite) 
console.log(colors3)

let colors4 = ["blue", "yellow", "green" ]; 
colors.shift() 
console.log(colors4) 

const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
 let myWatchedSeriesLength = myWatchedSeries.length
console.log(myWatchedSeriesLength)
let myWatchedLengthstring= myWatchedSeriesLength.toString()
console.log(myWatchedSeriesLengthstring)
let watched = "I watched ${myWatchedSeries.length} series: ${myWatchedSeriesLengthstring}"
console.log(watched)

let celsius = 37
let fahrenheit = celsius * 9/5 + 32
console.log(`${fahrenheit} F`);