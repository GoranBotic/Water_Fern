window.onload = function () {
    document.getElementById("assignmentPage").addEventListener("click", assignmentPage);
    document.getElementById("studentAssignments").addEventListener("click", studentAssignments);
    document.getElementById("report").addEventListener("click", assignmentPage);
    
    function assignmentPage() {
        location.href = "assignmentPage.html";
    }

    function studentAssignments() {
        location.href = "studentAssignments.html";
    }

    function reportViewer() {
        location.href = "reportViewer.html";
    }
}