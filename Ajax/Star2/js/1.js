function getMyColor() {
    $.ajax({
        type: "GET",
        // dataType: "json",
        url: "https://itc-colors.appspot.com/colors",
        success: function (response) {
            console.log("success");
            let mypictures = document.getElementById("images");
            response.forEach(element => {
                // images.innerHTML += element['name'];
                $("ul").append(`<li>${color["name"]}</li>`);
            });
        },
        error: function (response) {
            console.log("error");
        },
    });
}

function SetMyColor() {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "https://itc-colors.appspot.com/add_color",
        data: {
            color: $('#mycolor').val()
        },

        success: function (response) {
        },
        error: function (response) {
            console.log("error");
        },
        complete: function (response, status) {
            console.log("complete");
        }
    });
}






