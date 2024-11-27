$(document).ready(function () {
    getTARestState();

    $("#alertsButton").click(function (e)
    {
        showAlerts();
    });

    //$("#alerts-mobile-link").click(function (e) {
    //    $('#modalAlerts').foundation('reveal', 'open');
    //});

});


function getTARestState() {
    var sVal = "{nVersion:2}";
    try {
        $.ajax({
            type: "POST",
            url: wportalapps + "/lHomePageAlerts/TravelinAlerts.aspx/GetAlerts_Version",
            data: sVal,
            withCredentials: true,
            xhrFields: { withCredentials: true },
            contentType: "application/json;",
            dataType: "json",
            success: function (msg) {
                if (msg != null) {
                    if (msg.d != null) {                        
                        if (msg.d != "") {
                            if (msg.d.HasAlerts) {
				                $("#alertsButton").parent().show();
                                //check to see if the alert panel has been hidden
                                //update the indicator class on desktop
                                //$("#alertsButton").toggleClass("no-wsu-alert wsu-alert");
                                
                                //insert the desktop html content into the desktop interaction panel
                                $("#alertsDropdown").html(msg.d.RenderHTML);


                                if (getCookie("wsuAlerts") != "") {                                   
                                    //if it has been hidden, render a hidden panel
                                    $("#alertsDropdown").css("display", "none");

                                    $(document).click(function (e) {
                                        var container = $(".wsu-alert-dropdown, #alertsButton");

                                        if (!container.is(e.target) && container.has(e.target).length === 0) {
                                            $(".wsu-alert-dropdown").hide();

                                            if ($("#alertsButton").hasClass("active-icon")) {
                                                //$("#alertsButton").toggleClass("wsu-alert active-icon");
                                                $("#alertsButton").toggleClass("active-icon");
                                            };
                                        }
                                    });
                                }
                                else {
				                    //$("#alertsButton").parent().hide();
                                    $(".cover-icons").show();
                                    $("#mapsLink").css("opacity", ".3");
                                    $("#calendarLink").css("opacity", ".3");
                                    $("#notificationsButton").css("opacity", ".3");
                                    $("#azButton").css("opacity", ".3");
                                    $("#searchButton").css("opacity", ".3");
                                    $("#liProfile").css("opacity", ".3");
                                    $("#liLogin").css("opacity", ".3");
                                    showAlerts();
                                }                                
                            }
                            
                        }
                    }
                }
            },
            error: function (err) {
                //$("#login-profile-desktop-link").html(renderDirectLink());
            },
            failure: function (err) {
                //$("#login-profile-desktop-link").html(renderDirectLink());
            }
        });

    }
    catch (err) {
        //$("#login-profile-desktop-link").html(renderDirectLink());
    }

}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires + ";domain=.weber.edu;path=/";
}

function dismissAlerts() {
    setCookie("wsuAlerts", "true", 1);
    $("#alertsDropdown").hide();
    //commented out by cg 6/5/17
    //$('#modalAlerts').foundation('reveal', 'close');
	
	//added by ech 6/4
	$(".cover-icons").hide();

	$("#mapsLink").css("opacity", "1");
	$("#calendarLink").css("opacity", "1");
	$("#notificationsButton").css("opacity", "1");
	$("#azButton").css("opacity", "1");
	$("#searchButton").css("opacity", "1");
	$("#liLogin").css("opacity", "1");
	$("#liProfile").css("opacity", "1");

    //$("#alertsButton").toggleClass("wsu-alert active-icon");
	$("#alertsButton").toggleClass("active-icon");

	$(document).click(function (e){
		var container = $(".wsu-alert-dropdown, #alertsButton");
	
		if (!container.is(e.target)	&& container.has(e.target).length === 0){
			$(".wsu-alert-dropdown").hide();

			if($("#alertsButton").hasClass("active-icon")){
			    //$("#alertsButton").toggleClass("wsu-alert active-icon");
			    $("#alertsButton").toggleClass("active-icon");
			};
		}
	});
}

function showAlerts() {
    $(".wsu-alert-dropdown").fadeToggle("fast");
	$(".wsu-alert-dropdown").focus();
	$("#alertsButton").toggleClass("active-icon");
}

