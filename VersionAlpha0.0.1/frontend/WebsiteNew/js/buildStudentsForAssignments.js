
function buildStudentsList() {

   let assign = $.cookie("assign");
   let courseId = $.cookie("courseId");
   let list = assignlist();

   let studentList = document.getElementById("student-list");
   studentList.innerHTML = "";

   for (let i = 0; i < list.length; i++) {
      let li = buildList(list[i]);
      studentList.appendChild(li);
   }

}
buildStudentsList();

function buildList(item) {

   let li = document.createElement("li");
   li.setAttribute("onclick", "goToReport("+item.assignId+")");
   let text = document.createTextNode(item.name);

   li.appendChild(text);

   return li;

}

function goToReport(id) {

   $.cookie("assignId", id, {
      expires : 10,
      path    : '/'
   });
   
   window.open("reportViewer.html", "_self");

}