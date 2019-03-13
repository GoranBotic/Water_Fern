function viewReport(submissionID) {
    //Here we would again have an ajax call to get a list similar code from the data base 
    //For now I'm just going to use some hardcoded values
    //see classPage/classPage.js for an example of the ajax call 
    //the endpoint for this page will be 
    //  api/v1/getAssociations
    //  set a field called submissionID
    //we also need to use an endpoint call /apt/v1/getSubmission to get the actual files 

    //Get associations will return a list in the following format 
    //lineStartFile1, lineEndfile1, file2ID, lineStartFile2, lineEndfile2, score 
    //associations = [[0,0,1,2,2,0.98],[1,1,1,1,1,0.90], [2,2,1,0,0,0.65]]
    var associations 
    $.ajax({
        url: '/api/v1/getAssociations',
        type: 'POST',
        data: {
            "fID": submissionID
        },
        async: false, 
        success: function(fl) {
            alert(fl.associations)
            associations = fl.associations
        }
    });

    file1 = ["line1", "line2", "line3", "line4"]
    

    //Here we make a synchrous ajax request so that we can make sure the original source file loads before we start highlightling lines or anything 
    //notice the async:false 
    //Its true by default
    $.ajax({
        url: '/api/v1/getSubmission',
        type: 'POST',
        data: {"submissionID": submissionID
        },
        async: false, 
        success: function(fl) {
             file1 = fl.submission[1].split("\n")
        }
    });

    doc = $("<div/>")
    col1 = $("<div/>")
    col1.css("float", "left")
    col1.css("width", "50%")
    col1.attr("id", "orig")
    doc.append(col1) 
    col2 = $("<div/>")
    col2.css("float", "left")
    col2.css("width", "50%")
    col2.attr("id", "other")
    doc.append(col2)

    file1.forEach(function(l) {
        line = $("<span/>")
        line.text(l) 
        col1.append(line) 
        col1.append($("<br/>"))
    })

    alert(associations)
    associations.forEach(function(ass){
        for(var i = ass[0]; i <= ass[1]; i++) {
            col1.children().eq(i*2).css("background-color", "#ffdddd")
            col1.children().eq(i*2).attr("onclick", "loadSimilarAssignment(" + ass[2] + "," + ass[3] + "," + ass[4] + ")")
        }
    })

    doc.appendTo('body');

}

function loadSimilarAssignment(id, lineStart, lineEnd) {
    $("#other").remove();

    col2 = $("<div/>")
    col2.css("float", "left")
    col2.css("width", "50%")
    col2.attr("id", "other")
    doc.append(col2)

    //need a synchronous ajax call here 
    file2 = ["line3", "line2", "line1", "line5"]
    file2.forEach(function(l) {
        line = $("<span/>")
        line.text(l) 
        col2.append(line) 
        col2.append($("<br/>"))
    })

    for(var i = lineStart; i <= lineEnd; i++) {
        col2.children().eq(i*2).css("background-color", "#ffdddd")
    }

}