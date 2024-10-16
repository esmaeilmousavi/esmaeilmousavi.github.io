var Version_TravelinLogin = "2";
//scripts specifically associated with the identity and login processes
$(document).ready(function () {
    //$("#profileDropdown").append("<div id='pnlProfileInteractionDesktop'></div>");
    getRestState();

    $("#btnProfile").click(function (e)
    {
        getActiveState();                               
    });
            
});

function getRestState() {
    var sVal = "{nVersion:"+Version_TravelinLogin+"}";
    try {
        $.ajax({
            type: "POST",
            url: wportalapps + "/lpersonal_profile/TravelingProfile.aspx/GetRestState_Version",
            data: sVal,
            withCredentials: true,
            xhrFields: { withCredentials: true },
            contentType: "application/json;",
            dataType: "json",
            success: function (msg) {
                if (msg != null) {
                    if (msg.d != null) {
                        //$("#loginLink").html(msg.d.RenderHTML);
                        if (msg.d.RenderHTML == "logged out")
                        {
                            $("#liLogin").show();
                            $("#liProfile").hide();
                        }
                        else
                        {
                            $("#liLogin").hide();
                            $("#btnProfile").html(msg.d.RenderHTML);
                            $("#liProfile").show();
                        }
                        //if ($("#loginLink") != null)
                        //{
                        //    if ($("#loginLink:first-child") != null) {
                        //        GetUserState($("#loginLink:first-child"));
                        //    }
                        //}
                        
                    }
                }
            },
            error: function (err) {
                $("#loginLink").html(renderDirectLink());
                if ($("#loginLink:first-child") != null) {
                    GetUserState($("#loginLink:first-child"));
                }
            },
            failure: function (err) {
                $("#loginLink").html(renderDirectLink());
                if ($("#loginLink:first-child") != null) {
                    GetUserState($("#loginLink:first-child"));
                }
            }
        });

    }
    catch (err) {
        $("#loginLink").html(renderDirectLink());
        if ($("#loginLink:first-child") != null) {
            GetUserState($("#loginLink:first-child"));
        }
    }
     
}

function renderDirectLink()
{
    return "<div id='icoUnauthenticated icoDirectLink' class='logged-out-icon' onclick='self.location.href=\"" + wportalapps + "/eweber/default.aspx?usecas=true\"'></div>"
}

function GetUserState(obj) {
    //$(obj).clone().appendTo("div.chardinjs-helper-layer.chardinjs-left").css("right", "-8px").css("top", "0px");
}

function getActiveState() {
    //alert('getactivestate');
    var nWidth = $(document).width();
    nWidth = Math.round(nWidth);
    var sVal = "{nVersion:" + Version_TravelinLogin + ",Width:'" + nWidth + "'}";
    $.ajax({
        type: "POST",
        url: wportalapps + "/lpersonal_profile/TravelingProfile.aspx/GetActiveState_Version",
        data: sVal,
        withCredentials: true,
        xhrFields: { withCredentials: true },
        contentType: "application/json;",
        dataType: "json",
        success: function (msg) {
            if (msg != null) {
                if (msg.d != null) {
                    if (msg.d.RenderHTML == "send to eweber")
                    {
                        //no action needed
                        //self.location.href = "https://portalapps-dev.weber.edu/eweber";
                    }
                    else
                    {
                        //$("#btnProfile").toggleClass("active-icon");
                        $("#profileDropdown").html(msg.d.RenderHTML);
                        $("#profileDropdown").show();
                    }
                    
                }
            }
        }
    });

}

