let art = document.getElementsByTagName('article')[0];
console.log(art)

console.log(art.firstElementChild)

let p = document.getElementsByTagName('p')[3];
p.remove();

let h = document.getElementsByTagName('h2')[0];
h.addEventListener("click", set);

function set(){
    this.style.color = "red";  
}

let p1 = document.getElementsByTagName('h3')[0];
p1.addEventListener("click", clicked);

function clicked(){
    this.style.display = "none";
}

let btn = document.getElementById('btn');
let p2 = document.querySelectorAll('p');

btn.addEventListener("click", press);

function press(){
    for( let i = 0; i < p2.length; i++){
    p2[i].style.fontWeight = "bold";
    }
}

let p3 = document.getElementsByTagName('p')[2];
p3.addEventListener("click", fadeout);

function fadeout(){
    p3.style.opacity = "0.6";
}

