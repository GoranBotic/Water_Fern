function viewSubmissionList(ID){
    //Here we would again have an ajax call to get a list of submissions from the database
    //For now I'm just going to use some hardcoded values
    //see classPage/classPage.js for an example 
    //the endpoint for this page will be 
    //  api/v1/getSubmissionsList
    //  set a field called assignmentID 
    $.ajax({
        type: "POST",
        url: "/api/v1/getSubmissionsList",
        data: {
            'assignmentID': ID
        },
        success: function(theList){
            submissions = theList.assignment
            listToDisplay = $('<table/>')
            listToDisplay.attr("width", "100%");
            for(var i = 0; i < submissions.length; i++) {
                el = submissions[i];
                next = $("<tr/>");
                head = $("<th>" + el[0] + "</th>");
                next.append(head);
                head = $("<th>" + el[1] + "</th>");
                next.append(head);
                //red = 255.0*(1-el[4]);
                red = 255
                hex = Math.floor(red).toString(16)
                if(hex.length == 1){
                    hex = "0" + hex
                }
                color = "#ff" + hex + hex;
                next.css("background-color", color);
                next.attr("onclick", "viewReport(" + el[2] + ")");
                listToDisplay.append(next);
            }
            listToDisplay.appendTo('body');
        }
    });

    // //format for each row [user, filename, id, score] 
    // submissions = [["cody", "memes.java", 0, 0.98],["cody", "meme.java", 1, 0.98],["patrick", "somenam", 2, 0.10]]
    // //you can assume that assigments will be returned in order of most suspicious 
    // listToDisplay = $('<table/>')
    // listToDisplay.attr("width", "100%");
    // for(var i = 0; i < submissions.length; i++) {
    //     el = submissions[i];
    //     next = $("<tr/>");
    //     head = $("<th>" + el[0] + "</th>");
    //     next.append(head);
    //     head = $("<th>" + el[1] + "</th>");
    //     next.append(head);
    //     red = 255.0*(1-el[4]);
    //     hex = Math.floor(red).toString(16)
    //     if(hex.length == 1){
    //         hex = "0" + hex
    //     }
    //     color = "#ff" + hex + hex;
    //     next.css("background-color", color);
    //     next.attr("onclick", "viewReport(" + el[3] + ")");
    //     listToDisplay.append(next);
    // }
    // listToDisplay.appendTo('body');
}

function viewReport(ID) {
    $.cookie("submission", ID, {expires:10,path: '/'});
    window.location.replace("../reportViewer/reportViewer.html");
}
