// Return a filtered list of files as an array
module.exports.myFunction = function (directoryName, extension, callback){
    
    var fs = require('fs');
    var matchArray = [];
    var errorObj = {};

    fs.readdir(directoryName, (error, data) => {

        errorObj = error;

        data.forEach(function(index){
        
            if (index.includes("." + extension)){
                matchArray.push(index);
            }
    
        });

    });

    return (errorObj, matchArray);

}