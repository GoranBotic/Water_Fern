function displaySubmissionA(){
    let sida = $.cookie("submissionA");
    let report = $("#reportleft");
    report.html("");

    let sub = submission(sida);
    $("#name1").html(sub[0])
    let line_list = sub[1].split(/\r?\n/);
    for(var line in line_list){
        let lineelem = $('<a id="'+line+'a" class="line" href=""></a>');
        lineelem.html("<pre>"+line_list[line]+"</pre>");
        report.append(lineelem);
    }

    for(var i=0; i<50; i++){
        let lineelem = $('<a id="'+line+'b" class="line" href=""></a>');
        report.append(lineelem);
    }

}

function displaySubmissionB(sidb){
    let report = $("#reportright");
    report.html("");

    let sub = submission(sidb);
    $("#name2").html(sub[0])
    let line_list = sub[1].split(/\r?\n/);
    for(var line in line_list){
        let lineelem = $('<a id="'+line+'b" class="line" href=""></a>');
        lineelem.html("<pre>"+line_list[line]+"</pre>");
        report.append(lineelem);
    }

    for(var i=0; i<50; i++){
        let lineelem = $('<a id="'+line+'b" class="line" href=""></a>');
        report.append(lineelem);
    }

    buildSideSubmissionsList(sidb);

    let sida = $.cookie("submissionA");
    displaySubmissionA(); //clear first display of associations
    updateAssociations(sida,sidb); //add back associations
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