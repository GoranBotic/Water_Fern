function getAssignmentList(offeringID) {
    //This is what the call to the endpoint would look like 
    //The end point will return this list [["MemesAssign1", 0],["MemesAssign2", 1],["MemesAssign3", 2],["FuckMe", 3]]
    $.ajax({
        type: "POST",
        url: "/api/v1/getAssignmentList",
        data: {
            'offeringID': offeringID
        },
        success: function(theList){
            theList = theList.assignment
            toRet = $("<ul/>")
            for(var i = 0; i < theList.length; i++) {
                el = theList[i]; 
                next = $("<li/>");
                button = $("<button/>");
                button.attr('type', 'button');
                button.attr('value', el[0]);
                button.text(el[0])
                button.attr('onclick', 'viewAssignment(' + el[0]+')');
                next.append(button);
                toRet.append(next);
            }
            toRet.appendTo('body');
        }
    });

    //TO TEST THIS WITHOUT THE FRONT-END SERVER Running comment out the ajax thing and uncomment the stuff bellow 
    // theList = [["MemesAssign1", 0],["MemesAssign2", 1],["MemesAssign3", 2],["FuckMe", 3]]
    // toRet = $("<ul/>")
    //         for(var i = 0; i < theList.length; i++) {
    //             el = theList[i]; 
    //             next = $("<li/>");
    //             button = $("<button/>");
    //             button.attr('type', 'button');
    //             button.attr('value', el[0]);
    //             button.attr('onclick', 'viewAssignment(' + el[1]+')');
    //             next.append(button);
    //             toRet.append(next);
    //         }
    //         toRet.appendTo('body');
}

function viewAssignment(assignID) {
    $.cookie("assignment", assignID, {expires:10,path: '/'});
    window.location.href = "../assignmentList/assignmentList.html";
}