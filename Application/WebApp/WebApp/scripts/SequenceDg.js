//document.getElementById("btnHomeButton").onclick = function () {
//    window.location.href = "/Home/Index";
//}


function NavigateToHome() {
    $('#btnHomeButton').click(function () {
        window.location.href = "/Home/Index";
    });
}

function AskQuestion() {
    var question = $("#askQuestion").value();

}
