$(function(){

    // Google Maps API Variables
    var longitude;
    var latitude;
    var mapURL;

    // Weather Maps API Variables
    var $weatherLocation;
    var $weatherURL;

    $("#button").click(function(event){

        event.preventDefault();
        
        // Fetch API, Pass to main if success, otherwise display error
        $weatherLocation = $("#search-field").val();
        $weatherURL = `http://api.openweathermap.org/data/2.5/weather?q=${$weatherLocation}&appid=b4fcbd99cd57ef92fe14098cfe890cb2`;

        $.get($weatherURL)
        .done(function(weatherObj) {

            console.log(weatherObj);
            updateSuccess(weatherObj)	
        })
        .fail(function(error) {
            
            console.log(error);
            updateUIError()	
        });
    });


    //handle XHR success
    function updateSuccess(weatherObj) {

        var condition = weatherObj.weather[0]["main"];

        var degC = weatherObj.main["temp"] - 273.15;
        var degCInt = Math.floor(degC);

        var degF = degC * 1.8 + 32;
        var degFInt = Math.floor(degF);

        var $mapFrame = $("#mapFrame");
        var weatherBox = document.getElementById("weather");
        var $weatherImage = $("#weatherImage");

        longitude = weatherObj.coord["lon"];
        latitude = weatherObj.coord["lat"];

        mapURL = `https://www.google.com/maps/embed/v1/place?key=AIzaSyDffw0066YqW6BxV8Smx-oBzvX6UMkNTUY&q=${latitude},${longitude}&zoom=14&maptype=roadmap`;

        $mapFrame.attr("src", mapURL);
        
        weatherBox.innerHTML = "<p>" + degCInt + "&#176; C / " + degFInt + "&#176; F</p><p>" + condition + "</p>";

        // Weather Condition Image
        switch (condition){
            case "Clouds":
                $weatherImage.attr("src", "https://www.gov.gg/govgg1/images/weather/f.svg");
                break;

            case "Clear":
                $weatherImage.attr("src", "https://www.weatherusa.net/assets/icons/metar/hd/clear.png");
                break;

            case "Rain":
                $weatherImage.attr("src", "https://cdn0.iconfinder.com/data/icons/weather-2/80/Weather_forecast-04-512.png");
                break;

            case "Thunderstorm":
                $weatherImage.attr("src", "https://cdn2.iconfinder.com/data/icons/weather-24/256/Storm-512.png");
                break;

        }
            



    }

    // Upon XHR Error
    function updateUIError() {
        var $weatherBox = $('#weather');
        $weatherBox.addClass('hidden');
    }
});