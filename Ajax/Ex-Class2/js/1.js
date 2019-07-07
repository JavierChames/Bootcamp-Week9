$.ajax({
    type: "GET",
    dataType: "json",
    url: "http://itc-colors.appspot.com/get_images",
    success: function (response) {
        console.log("success");
        console.log(response);
        let mypictures=document.getElementById("images");
        for(let i=0;i<response.length;i++)
        {
            // mypictures.innerHTML += `<img src=${response[i]}></img>`
            var newImg = document.createElement("img");
            newImg.setAttribute('src',response[i])
            mypictures.appendChild(newImg);

        }
    },
    error: function (response) {
        console.log("error");
    },
    complete: function (response, status) {
        console.log("complete");
        // let jsonAsString = JSON.stringify(response);
        // console.log(jsonAsString);


    }
});
