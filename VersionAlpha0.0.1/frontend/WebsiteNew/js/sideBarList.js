
function buildSideBar() {

   let courseList = courses();
   let sideList = document.getElementById("side-list");
   sideList.innerHTML = "";

   // title li
   let header = document.createElement("li");
   header.setAttribute("class", "selection-list-title");
   let headText = document.createTextNode("COURSE LIST");
   header.appendChild(headText);

   sideList.appendChild(header);

   for (let i = 0; i < courseList.length; i++) {
      var course = buildSideCourseList(courseList[i]);
      sideList.appendChild(course);
   }

}
buildSideBar();

function buildSideCourseList(course) {

   let li = document.createElement("li");
   li.setAttribute("class", "selection-list");
   li.setAttribute("onclick", "goToCourse('"+course.id+"')");

   let text = document.createTextNode(course.name);

   li.appendChild(text);

   return li;

}

function goToCourse(id) {

   $.cookie("courseId", id, {
      expires : 10,
      path    : '/'
   });
   // document.cookie = "courseId="+id+"; path=/";

   window.open("assignmentPage.html", "_self");

}