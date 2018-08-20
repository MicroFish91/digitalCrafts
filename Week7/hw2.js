// Exercise 1
// var readline = require('readline');
// var fs = require('fs');

// var rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question("Filename? ", function(answer) {

//     fs.readFile(answer, (error, data) => {
        
//         if (error) {
//             console.error(error.message);
//             return;
//         }

//         console.log(data.toString().toUpperCase());

//     });

//     rl.close();
// });


// Exercise 2
var readline = require('readline');
var fs = require('fs');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("URL? ", function(answer) {

    fs.get(answer, (error, response, html) => {
        
        if (error) {
            console.error(error.message);
            return;
        }

        console.log(html);

    });

    rl.close();
});