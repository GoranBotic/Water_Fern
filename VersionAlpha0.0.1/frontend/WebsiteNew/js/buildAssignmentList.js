
function buildAssignmentList() {

   // let cookie = document.cookie;
   // let getCourse = cookie.split("; ")[0];
   // let getCourseNum = getCourse.split("=");
   let courseId = $.cookie("courseId");

   let assignList = listOfAssignments(courseId);
   let content = document.getElementById("assign-list");
   content.innerHTML = "";

   for (let i = 0; i < assignList.length; i++) {
      let assign = buildAssignment(courseId, assignList[i]);
      content.appendChild(assign);
   }

}
buildAssignmentList();

function buildAssignment(id, assign) {

   let li = document.createElement("li");
   li.setAttribute("onclick", "goToAssignList('"+id+"', "+assign+")");

   let text = document.createTextNode("Assignment "+assign);

   li.appendChild(text);

   return li;

}

function goToAssignList(id, assign) {

   document.cookie = "assign="+ assign;

   $.cookie("assign", assign, {
      expires : 10,
      path    : '/'
   });

   window.open("studentAssignments.html", "_self");

}