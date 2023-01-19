//translator
let lang = prompt("Enter your language");
console.log(lang.toLowerCase());
switch (lang) {
    case 'French':
        console.log("Bonjour");
        break;
    case 'English':
        console.log("Hello");
        break;
    case 'Hebrew':
        console.log("Shalom");
        break;
}

//grade
let g = parseInt(prompt("Enter  your grade?"));
if(g >= 90){
    console.log("A")
}
else if(g <= 90 && g >= 80){
    console.log("B")
}
else if(g <= 80 && g>= 70){
    console.log("C")
}
else if(g <= 70){
    console.log("D")
}



//verbing
let v = (prompt("The string is:"));
let m = (v + 'ing');
console.log(m)
let z = (m + 'ly')
console.log(z)
