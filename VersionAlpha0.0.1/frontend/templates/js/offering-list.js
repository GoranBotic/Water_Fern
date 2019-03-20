function buildOfferingList() {
    let courseId = $.cookie("courseId");
 
    let offList = offerings(courseId);
    let content = document.getElementById("assign-list");
    content.innerHTML = "";
 
    for (let i = 0; i < offList.length; i++) {
       let off = buildOffering(offList[i]);
       content.appendChild(off);
    }
 
}
 
function buildOffering(offering) {
 
    let li = document.createElement("li");
    li.setAttribute("onclick", "goToAssignList("+offering[0]+")");
 
    let text = document.createTextNode(offering[1]);
 
    li.appendChild(text);
 
    return li;
}

function goToAssignList(offering) {
 
    // document.cookie = "offering="+ offering;
 
    $.cookie("offeringId", offering, {
       expires : 10,
       path    : '/'
    });
 
    window.open("assignmentPage.html", "_self");
}