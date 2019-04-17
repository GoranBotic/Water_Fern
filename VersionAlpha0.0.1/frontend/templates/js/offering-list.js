function buildOfferingList() {
    let courseId = $.cookie("courseId");
 
    let offList = offerings(courseId);
    let content = document.getElementById("assign-list");
    content.innerHTML = "";
 
    content.appendChild(buildAddOfferingButton())
    for (let i = 0; i < offList.length; i++) {
       let off = buildOffering(offList[i]);
       content.appendChild(off);
    }
 
}

function buildAddOfferingButton(){
    let li = document.createElement("li");
    li.setAttribute("onclick", "postCreateOffering()");
 
    let text = document.createTextNode("+Add New Offering");
 
    li.appendChild(text);
 
    return li;
}

function postCreateOffering() {
    let courseId = $.cookie("courseId");
    $.ajax({
        type: "POST",
        url: "/api/v1/makeOffering",
        data: {
            'cid': courseId
        },
        async:false,
        success: function(data, status){
            if(status == "success") {
                window.open("offeringPage.html", "_self");
            } else {
                alert(data)
            }
        }
    })
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