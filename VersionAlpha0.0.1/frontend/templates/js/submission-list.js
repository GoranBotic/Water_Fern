
function buildSubmissionsList() {

    let assign = $.cookie("assign");
    let courseId = $.cookie("courseId");
    let list = submissions(assign);
 
    let studentList = document.getElementById("student-list");
    studentList.innerHTML = "";
 
    for (let i = 0; i < list.length; i++) {
       let li = buildSubmissions(list[i]);
       studentList.appendChild(li);
    }
 
}
 
function buildSubmissions(item) {
 
    let li = document.createElement("li");
    li.setAttribute("onclick", "goToReport("+item[0]+")");
    let text = document.createTextNode(item[1]);
 
    li.appendChild(text);
 
    return li;
 
}
 
function goToReport(id) {
 
    $.cookie("submissionA", id, {
       expires : 10,
       path    : '/'
    });
    
    window.open("reportPage.html", "_self");
 
}

//-----------------------------------------------------------------------------

function buildSideSubmissionsList(sel=-1) {
    let assign = $.cookie("assign");
    let sida = $.cookie("submissionA");
    let list = submissions(assign);

    let sideList = document.getElementById("side-list");
    sideList.innerHTML = "";

    // title li
    let header = document.createElement("li");
    header.setAttribute("class", "selection-list-title");
    let headText = document.createTextNode("SUBMISSIONS");
    header.appendChild(headText);

    sideList.appendChild(header);
 
    for (let i = 0; i < list.length; i++) {
        if(list[i][0] != sida){
            let sub = buildSideSubmissions(list[i],sel);
            sideList.appendChild(sub);
        }
    }
 
}
 
function buildSideSubmissions(sub,sel) {
 
    let li = document.createElement("li");
    li.setAttribute("class", "selection-list");
    li.setAttribute("onclick", "displaySubmissionB("+sub[0]+")");
 
    let text = document.createTextNode(sub[1]+": "+sub[2]+" "+sub[3]);

    if(sub[0] == sel){
        li.setAttribute("class", "selection-list selected");
    }
 
    li.appendChild(text);
 
    return li;
 
}