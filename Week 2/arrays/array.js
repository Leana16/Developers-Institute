let f = 'choclate';
let m = 'dinner';
console.log("I eat" + " " + f + " " + "at" + " " + "every" + " "+ m)

let celsius = 37;
let fahrenheit = celsius * 9/5 + 32;
console.log(`${fahrenheit} F`);


let age1 = 20

if (age === 18) {
    console.log("It's your birthday !!") 
} else if (age > 18) {
    console.log("We can go to a pub together !!")
} else {
    console.log("Sorry...You have to stay at home tonight")
}


let age = parseInt(prompt("How old are you?"));
  if(age < 18) {
    alert("sorry, you are too young to drive this car. Powering off");
  }
  else if(age === 18){
    alert("Congratulations on your first year of driving. Enjoy the ride!")
  }
  else{
    alert( "Powering On. Enjoy the ride!")
  }


  let fruit = 'Papayas';

switch (fruit) {
  case 'Oranges':
    console.log('Oranges are $0.59 a pound.');
    break;
  case 'Mangoes':
  case 'Papayas':
    console.log('Mangoes and papayas are $2.79 a pound.');
    // expected output: "Mangoes and papayas are $2.79 a pound."
    break;
  default:
    console.log('Sorry, we are out of ' + fruit + '.');
}

//fruit
let fruit = 'Papayas';

switch (fruit) {
  case 'Oranges':
    console.log('Oranges are $0.59 a pound.');
    break;
  case 'Mangoes':
  case 'Papayas':
    console.log('Mangoes and papayas are $2.79 a pound.');
    // expected output: "Mangoes and papayas are $2.79 a pound."
    break;
  default:
    console.log('Sorry, we are out of ' + fruit + '.');
}

//numbers
let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}

let b = 2 + 3;

switch (b) {
  case 4:
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}