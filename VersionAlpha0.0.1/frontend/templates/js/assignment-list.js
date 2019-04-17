
function buildAssignmentList() {
    let offeringId = $.cookie("offeringId");
 
    let assignList = assignments(offeringId);
    let content = document.getElementById("assign-list");
    content.innerHTML = "";
 
    content.appendChild(buildAddAssignmentButton())

    for (let i = 0; i < assignList.length; i++) {
       let assign = buildAssignment(assignList[i]);
       content.appendChild(assign);
    }
 
}

function buildAddAssignmentButton(){
    let li = document.createElement("li");
    li.setAttribute("onclick", "postCreateAssignment()");
 
    let text = document.createTextNode("+Add New Assignment");
 
    li.appendChild(text);
 
    return li;
}

function postCreateAssignment() {
    let oId = $.cookie("offeringId");
    $.ajax({
        type: "POST",
        url: "/api/v1/makeAssignment",
        data: {
            'oid': oId
        },
        async:false,
        success: function(data, status){
            if(status == "success") {
                window.open("assignmentPage.html", "_self");
            } else {
                alert(data)
            }
        }
    })
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