function move() {

  var elem = document.getElementById("myBar");
  var width = 0;
  var old_width = 0;
  var rep = 0;
  var id = setInterval(frame, 1000);
  function frame() {
    if (width >= 100) {//endpoint is an estimate, if it stagnates then it is done
      clearInterval(id);

      window.location.href = 'submissionsPage.html';
      
    } else {
      // width++;
      old_width = width;
      let assId = $.cookie("assign");
      width = progress(assId)*100.0;//mabye not hardcode this?
      console.log(width);

      if(width == old_width){
        rep = rep + 1
      }else{
        rep = 0;
      }

      elem.style.width = (width + (0.025*rep)) + '%';
    }
  }
}