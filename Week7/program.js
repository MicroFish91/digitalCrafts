// Exercise 1
// console.log("HELLO WORLD");

// Exercise 2
// Takes the process.argv property 
// function sumNumber(myArray){
    
//     var sum = 0;

//     for(let x = 2; x < myArray.length; x++){
//         sum += parseInt(myArray[x]);
//     }

//     return sum;

// }

// console.log(sumNumber(process.argv));

// Exercise 3
// var fs = require('fs');

// var str = (fs.readFileSync(process.argv[2])).toString();

// str = str.split('\n');

// console.log(str.length - 1);

// Exercise 4
// var fs = require('fs');

// fs.readFile(process.argv[2], 'utf8', (error, data) => {
//     console.log(data.split('\n').length - 1);
// });

// Exercise 5 

// 1st argument: directory [2]
// 2nd argument: extensions to look for [3]

// var fs = require('fs');

// fs.readdir(process.argv[2], (error, data) => {
    
//     data.forEach(function(index){
        
//         if (index.includes("." + process.argv[3])){
//             console.log(index);
//         }

//     });

// });

// Exercise 6
// Prints a list of files in a given directory, filtered by extension of the files
// First argument is the directory name

var exported = require("./module.js");

exported.myFunction(process.argv[2], process.argv[3], (error, data) => {
    for(let file in data){
        console.log(data[file]);
    }
});