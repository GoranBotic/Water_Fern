function move() {


  var elem = document.getElementById("myBar");
  var width = 1;
  var id = setInterval(frame, 10);
  function frame() {
    if (width >= 100) {
      clearInterval(id);
      window.location.href = 'submissionsPage.html';
      
    } else {
      width++;
      elem.style.width = width + '%';
    }
  }
}