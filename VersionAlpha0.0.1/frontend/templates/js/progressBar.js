function move() {

  var elem = document.getElementById("myBar");
  var width = 1;
  var old_width = 0;
  var id = setInterval(frame, 1000);
  function frame() {
    if (width >= 100 || old_width == width) {//endpoint is an estimate, if it stagnates then it is done
      clearInterval(id);

      window.location.href = 'submissionsPage.html';
      
    } else {
      // width++;
      old_width = width;
      width = progress(0)*100.0;//mabye not hardcode this?
      console.log(width);
      elem.style.width = width + '%';
    }
  }
}