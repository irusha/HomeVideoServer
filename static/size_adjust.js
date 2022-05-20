let video = this.document.getElementById('video_m')
window.onload = function () {
  video.setAttribute('width', document.body.clientWidth - 20)
}
window.addEventListener("resize", function (event) {
  console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight + ' high');

  video.setAttribute('width', document.body.clientWidth - 20)

})

c = true

function w3_open() {
  if (c) {
    document.getElementById("rightMenu").style.display = "block";

    c = false;
  }
  else {
    document.getElementById("rightMenu").style.display = "none";
    c = true;
  }

}