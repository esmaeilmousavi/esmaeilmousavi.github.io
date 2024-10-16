var notifications_version = 1;

$(document).ready(function ()
{
    if (isPresentNewLogin())
        {checkActionState();}

    //$("#notificationsButton").append("<div id='notificationsDropdown'></div>");
    getNNRestState();

    $("#notificationsButton").click(function (e)
    {
        getNNActiveState();
    });

    //$("#ewsm-mobile-link").click(function (e) {
        //getNNMobileActiveState();
    //    self.location.href = 'https://portalapps-dev.weber.edu/ewebersystemmessages/UserInterface.aspx';
    //});
});

function getNNRestState() {
    var sVal = "{nVersion:"+notifications_version+"}";
    try {
        $.ajax({
            type: "POST",
            url: wportalapps + "/ewebersystemmessages/PublicMethods.aspx/GetRestState_Version",
            data: sVal,
            withCredentials: true,
            xhrFields: { withCredentials: true },
            contentType: "application/json;",
            dataType: "json",
            success: function (msg) {
                if (msg != null) {
                    if (msg.d != null) {
                        if (msg.d.IsLoggedIn)
                        {
                            //$("#ewsm-desktop-link").html(msg.d.RenderHTML);
                            //$("#ewsm-desktop-link").css("display", "inline-block");
                            //$("#notificationsButton").attr("wsu-data", msg.d.RenderHTML);
                            $("#notificationsButton").parent().show();
                            $("#notificationsButton").append("<span id='notificationsCount'>" + msg.d.RenderHTML + "</span>");
                        }
                        else
                        {
                            $("#notificationsButton").parent().hide();
                        }
                    }
                }
            },
            error: function (err) {
                //$("#notificationsButton").html(renderNNDirectLink());
                //console.error("ajax error: " + err.msg)
            },
            failure: function (err) {
                //$("#notificationsButton").html(renderNNDirectLink());
                //console.error("ajax failure: " + err.msg)
            }
        });

    }
    catch (err) {
        //$("#notificationsButton").html(renderNNDirectLink());
        //console.error("ajax init error: " + err.msg)
    }

}

function clearMessages() {
    var sVal = "{}";
    try {
        $.ajax({
            type: "POST",
            url: wportalapps + "/ewebersystemmessages/PublicMethods.aspx/MarkAllSystemMessagesRead",
            data: sVal,
            withCredentials: true,
            xhrFields: { withCredentials: true },
            contentType: "application/json;",
            dataType: "json",
            success: function (msg) {
                //if (msg != null) {
                //    if (msg.d != null) {
                //        if (msg.d.IsLoggedIn) {
                //            $("#ewsm-desktop-link").html(msg.d.RenderHTML);
                //            $("#ewsm-desktop-link").css("display", "inline-block");
                //        }
                //    }
                //}
                //alert(msg.d);
            },
            error: function (err) {
                //alert('yo1');
            },
            failure: function (err) {
                //alert('yo2');
            }
        });

    }
    catch (err) {
        //alert('yo3');
    }

}


function getNNActiveState() {
    var sVal = "{nVersion:" + notifications_version + "}";
    $.ajax({
        type: "POST",
        url: wportalapps + "/ewebersystemmessages/PublicMethods.aspx/GetActiveState_Version",
        data: sVal,
        withCredentials: true,
        xhrFields: { withCredentials: true },
        contentType: "application/json;",
        dataType: "json",
        success: function (msg) {
            if (msg != null) {
                if (msg.d != null)
                {                   
                    $("#notificationsDropdown").html(msg.d.RenderHTML);
                    if (msg.d.RenderHTML != "")
                    {
                        $("#notificationsDropdown").css("display", "block");
                        clearMessages();
                    }
                }
            }
        }
    });

}


function renderNNDirectLink() {
    
}


function checkActionState()
{
    var sVal = "{}";
    $.ajax({
        type: "POST",
        url: wportalapps + "/ewebersystemmessages/PublicMethods.aspx/CheckLoginStack",
        data: sVal,
        withCredentials: true,
        xhrFields: { withCredentials: true },
        contentType: "application/json;",
        dataType: "json",
        success: function (msg)
        {
            removeActionState();
        }
    });
}

function removeActionState()
{
    document.cookie = "WSUAction=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;domain=.weber.edu";
}

function isPresentNewLogin()
{
    var rCookies = document.cookie.split(";");
    for (i = 0; i < rCookies.length; i++)
    {
        c = rCookies[i].split("=");
        if (c[0].trim() == "WSUAction" && c[1].trim() == "new login")
        {
            return true;
        }
    }

    return false;
}