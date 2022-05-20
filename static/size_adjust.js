let video = this.document.getElementById('video_m')
let thumbnails = this.document.getElementsByClassName('m_thumb_container')
window.onload = function () {

  try {
    if (document.body.clientWidth > 540) {
      for (let index = 0; index < thumbnails.length; index++) {
        const element = thumbnails[index];
        element.style.width = document.body.clientWidth - 60 + "px"
        element.style.margin = "20px";
      }
      
    }
    else{
      for (let index = 0; index < thumbnails.length; index++) {
        const element = thumbnails[index];
        element.style.width = document.body.clientWidth - 40 + "px"
        element.style.margin = "10px";
      }
    }

    video.setAttribute('width', document.body.clientWidth - 20)

  } catch (error) {

  }

}
window.addEventListener("resize", function (event) {
  console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight + ' high');

  try {
    if (document.body.clientWidth > 540) {
      for (let index = 0; index < thumbnails.length; index++) {
        const element = thumbnails[index];
        element.style.width = document.body.clientWidth - 60 + "px"
        element.style.margin = "20px";
      }
      
    }
    else{
      for (let index = 0; index < thumbnails.length; index++) {
        const element = thumbnails[index];
        element.style.width = document.body.clientWidth - 40 + "px"
        element.style.margin = "10px";
      }
    }

    video.setAttribute('width', document.body.clientWidth - 20)

  } catch (error) {

  }

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
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

function scroll_to_folders() {
  let e = document.getElementById("folders");
  e.scrollIntoView({
    block: 'start',
    behavior: 'smooth',
    inline: 'start'
  });
}