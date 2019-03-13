
let conts = assignContents();
let assignsList = assignlist();

function getReport(id, side) {

   let container = document.getElementById("report"+side);
   container.innerHTML = "";

   if (id < 0) {
      id = getSimilar(id);
   }

   let info = getInfo(id);

   let ul = document.createElement("ul");
   ul.setAttribute("class", "report-display");
   lines = info.line;

   for (let i = 0; i < lines.length; i++) {
      let li = document.createElement("li");
      let text = document.createTextNode(lines[i]);
      li.appendChild(text);
      ul.appendChild(li);
   }

   container.appendChild(ul);

}

getReport($.cookie("assignId"), "left");
getReport(-1, "right");

function getInfo(id) {

   for (let i = 0; i < conts.length; i++) {
      if (conts[i].assignId == id)
         return conts[i];
   }

}

function getSimilar(v) {

   // assignsList
   let id = (v * -1) - 1;
   let master = $.cookie("assignId");
   for (let i = 0; i < assignsList.length; i++) {
      if (assignsList[i].assignId == master) {
         return assignsList[i].similars[id];
      }
   }

   return null;

}