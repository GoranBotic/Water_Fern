
function displaySubmissionA(){
    let sida = $.cookie("submissionA");
    let report = document.getElementById("reportleft");
    report.innerHTML = "";

    // console.log("student1Id = "+student1Id);
    let name1 = document.getElementById("name1");
    var data = dummyData()[0];
    console.log(data);
    let text = document.createTextNode(data["name"]);
    name1.appendChild(text);

    let file = data.files[0].data;
    let div = document.createElement("div");
    
    for (let i = 0; i < file.length; i++) {
        div = document.createElement("div");
        // div.style.backgroundColor = 'hsl(0, 100%, '+(((i/file.length)*50)+50)+'%)';
        if (file[i] == "") {
            text = document.createTextNode(" ");
        } else {
            text = document.createTextNode(file[i]);
        }
        div.appendChild(text);
        report.appendChild(div);
    }

    // let line_list = submission(sida)[1].split(/\r?\n/);
    // for(var line in line_list){
    //     let lineelem = $('<a id="'+line+'a" class="line" href=""></a>');
    //     lineelem.html("<pre>"+line_list[line]+"</pre>");
    //     report.append(lineelem);
    // }

}
// displaySubmissionA();

function displaySubmissionB(sidb){
    let report = document.getElementById("reportright");
    report.innerHTML = "";

    let name2 = document.getElementById("name2");
    var data = dummyData()[1];
    console.log(data);
    let text = document.createTextNode(data.name);
    name2.appendChild(text);

    let file = data.files[0].data;
    let div = document.createElement("div");
    
    for (let i = 0; i < file.length; i++) {
        div = document.createElement("div");
        if (file[i] == "") {
            text = document.createTextNode(" ");
        } else {
            text = document.createTextNode(file[i]);
        }
        div.appendChild(text);
        report.appendChild(div);
    }

    // let line_list = submission(sidb)[1].split(/\r?\n/);
    // for(var line in line_list){
    //     let lineelem = $('<a id="'+line+'b" class="line" href=""></a>');
    //     lineelem.html("<pre>"+line_list[line]+"</pre>");
    //     report.append(lineelem);
    // }

    // let sida = $.cookie("submissionA");
    // displaySubmissionA(); //clear first display of associations
    // updateAssociations(sida,sidb); //add back associations
}

function buildSideSubmissionsList() {
    // get data.js
    // go through both students
    // get the files that are similar to each other
    // display the files for the first student that have a high similarity rate
    // make the file names clickable
    let data = dummyData();
}

function updateAssociations(sida, sidb){
    association_list = associations(sida, sidb);
  
    line_list = cleanAssociationOverlap(association_list);
   
    for(var line in line_list[0]){
        lineelem = $("#"+line);
        lineelem.addClass("linkline");
        lineelem.attr("href","#"+line_list[0][line][0]+"b");
    }
    for(var line in line_list[1]){
        lineelem = $("#"+line);
        lineelem.addClass("linkline");
        lineelem.attr("href","#"+line_list[1][line][0]+"a");
    }
}

//TODO: ehere 
function cleanAssociationOverlap(alist){
    suba_ass = {};
    subb_ass = {};

    for(var ass in alist){
        //generate all links for the left side
        for(let i = alist[ass][0]; i<alist[ass][1]; i++){
            key = i+"a";
            //if there is already a link from this line
            if(key in suba_ass){
                //if this new link has a greater association than the old one, replace
                if(suba_ass[key][1] > alist[ass][4]){
                    suba_ass[key] = [alist[ass][2],alist[ass][4]];
                }
            }else{
                //link to start line in second file
                suba_ass[key] = [alist[ass][2],alist[ass][4]];
            }
        }

        //generate all links for the right side
        for(let i = alist[ass][2]; i<alist[ass][3]; i++){
            key = i+"b";
            //if there is already a link from this line
            if(key in subb_ass){
                //if this new link has a greater association than the old one, replace
                if(subb_ass[key][1] > alist[ass][4]){
                    subb_ass[key] = [alist[ass][0],alist[ass][4]];
                }
            }else{
                //link to start line in first file
                subb_ass[key] = [alist[ass][0],alist[ass][4]];
            }
        }
    }

    return [suba_ass,subb_ass];
}