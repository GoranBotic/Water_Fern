
function buildAssignmentList() {
    let offeringId = $.cookie("offeringId");
 
    let assignList = assignments(offeringId);
    let content = document.getElementById("assign-list");
    content.innerHTML = "";
 
    for (let i = 0; i < assignList.length; i++) {
       let assign = buildAssignment(assignList[i]);
       content.appendChild(assign);
    }
 
}
 
function buildAssignment(assign) {
 
    let li = document.createElement("li");
    li.setAttribute("onclick", "goToAssignList("+assign+")");
 
    let text = document.createTextNode("Assignment "+assign);
 
    li.appendChild(text);
 
    return li;
}

function goToAssignList(assign) {
 
    // document.cookie = "assign="+ assign;
 
    $.cookie("assign", assign, {
       expires : 10,
       path    : '/'
    });
 
    window.open("submissionsPage.html", "_self");
}