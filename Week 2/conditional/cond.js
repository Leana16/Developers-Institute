//Exercise
//display the biggest number
let x = 6;
let y = 3
 if(x > y){
    console.log("x is the biggest number")
 }
 else{
    console.log("x is the lowest number")
 }

 
//even or odd
let c = parseInt(prompt("Print a number"));
let num  = (c % 2)
if(num == 0){
    console.log(`${c} is an even number`)
}
else{
    console.log(`${c} is an odd number`)
}


//group chat
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000", "jkfgwelufz", "hehfeério","jkwdgféw"];
console.log(users.length)
if(users.length === 0){
    consSole.log("no one is online")
}
 else if(users.length === 1){
    console.log(users3[0])
}
 else if(users.length === 2){
    console.log(users[0], ",", users[1])
}
else{
    console.log(users[0],",", users[1], ",",users[2], "and", users.length-3, "more are online")
}

//chichuachua
let newDog = "Chichuahua";
console.log(newDog.length)
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())
if(newDog === "Chichuahua"){
    console.log("I love Chihuahuas, it’s my favorite dog breed")
  }
  else{
    console.log("I dont care, I prefer cats")
  }