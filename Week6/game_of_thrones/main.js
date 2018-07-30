(function(){

    // Fetch Object
    $.get("https://www.anapioficeandfire.com/api/characters?page=1&pageSize=50").done(function(object){

        updateSuccess(object);

    })
    .fail(function(error){
        updateError();
    })

    function updateSuccess(object){
        console.log(object);

    }

    function updateError(){

    }


})();