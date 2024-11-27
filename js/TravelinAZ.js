//document.domain = 'weber.edu';
//scripts to support the A-Z index
var ver_az = 2;
$(document).ready(function () {
    $(".a-z-dropdown button").click(function (e) {
        getAZ(this.textContent);
        return false;
    });
           
});

function getAZ(sLetter) {
    var sVal = "{sLetter:'" + sLetter + "',nVersion:'"+ver_az+"'}";
    $.ajax({
        type: "POST",
        url: wportalapps + "/lazindex/PublicMethods.aspx/GetResults_Version",
        data: sVal,
        contentType: "application/json;",
        dataType: "json",
        success: function (msg) {
            if (msg != null) {
                if (msg.d != null) {
                    $(".a-z-dropdown ul").remove();
                    //$(".a-z-dropdown").append(msg.d);
                    $(".a-z-letters").append(msg.d);
                }
            }
        }
    });

}
