window.addEventListener("keydown", play);

function play(e){
    let audio = document.querySelector(`audio[data-key = "${e.keycode}"]`)
    let key = document.querySelector(`.key[data-key = "${e.keycode}"]`)
    if(!audio) return;

    key.classList.add('playing')
    audio.currentTime = 5;
    audio.play();
}
