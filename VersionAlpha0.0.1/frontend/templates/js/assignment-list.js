
//builds a list of assignments for a specific offering
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
 
//creates an element of the assignment list 
function buildAssignment(assign) {
 
    let li = document.createElement("li");
    li.setAttribute("onclick", "goToAssignList("+assign+")");
 
    let text = document.createTextNode("Assignment "+assign);
 
    li.appendChild(text);
 
    return li;
}

//sends the user to the list of submissions for an assignment
function goToAssignList(assign) {
 
    // document.cookie = "assign="+ assign;
 
    $.cookie("assign", assign, {
       expires : 10,
       path    : '/'
    });
 
    window.open("submissionsPage.html", "_self");
}