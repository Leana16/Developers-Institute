//display favorite color
let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(' '))

//mixup
let str1 = "mix";
let str2 = "pod";

let cmd1 = str1.slice(2)
let cmd2 = str2.slice(2)
let arr1 = str1.slice(0, 2) + cmd2
let arr2 = str2.slice(0, 2) + cmd1
console.log(arr1) 
console.log(arr2)

let arr = (`${arr1} , ${arr2}`)
console.log(arr)

//nums
let a = ["2", "3"];
console.log(2 + 3)

//nemo
/*let b = "Nemo";
let e = b.split('')
console.log(e)
let c = (`I love the movie named ${b}`)
console.log(c)
let d = b.indexOf("Nemo");
 console.log(d)
 if(b === "Nemo"){ 
    console.log(`I found Nemo at ${d}`)
 }
 else{
    console.log("I cant find Nemo")
 }*/

//boom
let num = parseInt(prompt("Print a number"));
if(num < 2){
    alert("boom")
}
else if(num % 2 == 0 && num % 5 == 0){
    alert("Boom".toUpperCase() + "!")
}
else if(num > 2){
    alert("B" + "o".repeat(num) + "m")
}
else if(num % 2 == 0){
    alert("Boom!")
}
else if(num % 5 == 0){
    alert("Boom".toUpperCase())
}
