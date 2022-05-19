var video = this.document.getElementById('video_m')
window.onload = function () {
    video.setAttribute('width', document.body.clientWidth - 20)
}
window.addEventListener("resize", function(event) {
    console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight+' high');
    
    video.setAttribute('width', document.body.clientWidth - 20)
    
  })

