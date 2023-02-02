//users xp
let demo = document.getElementById("container");
console.log(demo);

let li = document.getElementsByClassName("list")[0];
console.log(li)

let change = li.lastElementChild.innerHTML = "Richard";
console.log(change)

let all = document.querySelectorAll("li:first-child");
for(let al of all){
    console.log(al.innerHTML) 
    let a = al.innerHTML ="Leana"
    console.log(a)
}

let lis = document.getElementsByClassName("list")[1];
console.log(lis)

let del= lis.firstElementChild;
let det= del.nextElementSibling;
console.log(det.remove())

/*
console.log(del.removeChild(det));*/



//users and style xp
/*let user = document.getElementsByTagName("div")[0];
console.log(user);

let s = user.style.cssText = `background:lightblue; padding:10px`; 
console.log(s)

console.log(user.nextElementSibling)
let parent = user.nextElementSibling;
console.log(parent)

let f= parent.firstElementChild;
/*console.log(f.remove())
console.log(f.textContent)

le s2= f.style.display = "none";
console.log(s2)

let l = parent.lastElementChild;
console.log(l.textContent)

let s1= l.style.border = "thin solid grey";
console.log(s1)

let body = document.body.style.fontSize = "20px";
console.log(body)
   */ 
