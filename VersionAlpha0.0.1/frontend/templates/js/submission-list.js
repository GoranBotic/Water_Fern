
function buildSubmissionsList() {

    let assign = $.cookie("assign");
    let courseId = $.cookie("courseId");
    let list = submissions(assign);

    let studentList = document.getElementById("student-list");
    studentList.innerHTML = "";

    let highest = 0; //the highest score
    for (let i = 0; i < list.length; i++) {
        let li = buildSubmissions(list[i]);
        if (i == 0) {
            highest = li.getAttribute("score"); //the first score in the list will have the highest score
        }
        
        let col =(100+((li.getAttribute("score"))/highest)*(-50));
        li.style.backgroundColor = "hsl(0,100%, "+col+"%)"; //sets the coloring, with 1 giving a full red, the lowest being white
        // li.setAttribute("style","background_color : rgb(255,0,0);");
        studentList.appendChild(li);

    }
 
}

function buildSubmissions(item) {

    let li = document.createElement("li");

    li.setAttribute("onclick", "goToReport(" + item[0] + ")");
    let text = document.createTextNode(item[1] + " | " + item[3]);
    li.setAttribute("score", item[3]);//Math.log(item[3]/(1.0-item[3])));//gives each element an attribute called score

    li.appendChild(text);

    return li;

}

function goToReport(id) {

    $.cookie("submissionA", id, {
        expires: 10,
        path: '/'
    });

    window.open("reportPage.html", "_self");

}

//-----------------------------------------------------------------------------

function buildSideSubmissionsList() {
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
        if (list[i][0] != sida) {
            let sub = buildSideSubmissions(list[i]);
            sideList.appendChild(sub);
        }
    }

}

function buildSideSubmissions(sub) {

    let li = document.createElement("li");
    li.setAttribute("class", "selection-list");
    li.setAttribute("onclick", "displaySubmissionB(" + sub[0] + ")");

    let text = document.createTextNode(sub[1] + " : " + sub[2] + " " + sub[3]);

    li.appendChild(text);

    return li;

}