let h3 = document.getElementsByTagName('h3')[1];
h3.style.marginTop= "20px";
h3.style.wordSpacing = "1.5em";

let content = document.getElementsByClassName('content')[1];
content.style.margin = "12px";

let i=1
while(i < 4){
    document.write("<img src=./image10'"+i+".jfif>")
    i++
}

let h = document.getElementsByTagName('h2')[0];
h.addEventListener("click", click);

function click(){
    this.style.color = "black";
    document.getElementById('demo').innerHTML = "Y-Graphic Design";
    document.getElementById('demo').style.cssText = `color:red; background-color: black; text-align: center; font-size: 30px;   margin-top: 30px; 
    border-radius: 50%;`
}

 /*let img = document.getElementsByClassName('img');
 img.addEventListener('mouseover', function(){
    img.classList.add('zoomImg');
    img.classList.remove('img');
 })

 img.addEventListener('mouseout', function(){
    img.classList.remove('zoomImg');
    img.classList.add('img');
 })*/


/*let l= 3;
var img = new Image();
img.src = "./image10.jfif"
for( i = 0; i < 3; i++){
    document.body.appendChild(img);
    img.style.cssText = `width: 100px;`
}*/

