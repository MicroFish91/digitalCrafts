// Instantiate Variables
var images = document.querySelectorAll(".image3");

images.forEach(function(value){

    value.addEventListener("click", (e) => {

        document.querySelectorAll(".image1")[0].src = value.src;

        if (value.classList[0] == "highlight"){
            value.removeAttribute("class", "highlight");
        } else {
            value.setAttribute("class", "highlight");
        }


    });
});