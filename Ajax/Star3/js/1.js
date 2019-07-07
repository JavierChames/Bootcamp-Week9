$(document).ready(function () {
    getState();
});

setInterval(function () {
    getState()
}, 2000);

var currentstate = document.getElementsByClassName("state");
var currentmode = document.getElementsByClassName("mode");
var currentemp = document.getElementsByClassName("temp");



function getState() {
    $.ajax({
        type: "GET",
        dataType: "json",
        url: "https:///itc-colors.appspot.com/aircon/state",
        success: function (response) {
            let state = response['state'];
            let mode = response['mode'];
            let tmp = response['temp'];
            console.log(state);
            console.log(mode);
            console.log(tmp);

                if (state === "off") {
                    currentstate[0].style.backgroundImage = "url('./images/poweroff.png')";
                    currentmode[0].style.backgroundImage = "";
                    currentemp[0].innerHTML="";
                }
                if (state === "on") {
                    currentstate[0].style.backgroundImage = "url('./images/poweron.png')";
                    currentemp[0].innerHTML=tmp;

                }


                if (mode === "cool") {
                    currentmode[0].style.backgroundImage = "url('./images/cool.png')";
                }
                if (mode === "fan") {
                    currentmode[0].style.backgroundImage = "url('./images/fan.png')";
                }
                if (mode === "dry") {
                    currentmode[0].style.backgroundImage = "url('./images/dry.png')";
                }





        },
        error: function (response) {
            console.log("error");
        },
    });
}







