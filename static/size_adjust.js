let video = this.document.getElementById('video_m')
window.onload = function () {
  try {
    video.setAttribute('width', document.body.clientWidth - 20)
  } catch (error) {
    
  }
  
}
window.addEventListener("resize", function (event) {
  console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight + ' high');

  video.setAttribute('width', document.body.clientWidth - 20)

})

c = true

function w3_open() {
  if (c) {
    document.getElementById("rightMenu").style.display = "block";
    document.getElementById("menu_button").setAttribute('d', "M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z");
    c = false;
  }
  else {
    document.getElementById("rightMenu").style.display = "none";
    document.getElementById("menu_button").setAttribute('d', "M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z");
    c = true;
  }

}

function scroll_to_folders() {
  let e = document.getElementById("folders");
  e.scrollIntoView({
    block: 'start',
    behavior: 'smooth',
    inline: 'start'
  });
}