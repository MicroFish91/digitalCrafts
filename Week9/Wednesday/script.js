let express = require('express');
let app = express();
let axios = require('axios');
// var responses = [];

// var rp = require('request-promise');
// const fs = require('fs-extra');

// var url = [ 'https://en.wikipedia.org/wiki/Futures_and_promises', 'https://en.wikipedia.org/wiki/Continuation-passing_style', 'https://en.wikipedia.org/wiki/JavaScript', 'https://en.wikipedia.org/wiki/Node.js', 'https://en.wikipedia.org/wiki/Google_Chrome' ];

// var r1 = axios.get(url[0])
// .then(function(response){
//     responses[0] = response;
// })
// .catch(function(error){
//     console.log(error);
// });

// var r2 = axios.get(url[1])
// .then(function(response){
//     responses[1] = response;
// })
// .catch(function(error){
//     console.log(error);
// });

// var r3 = axios.get(url[2])
// .then(function(response){
//     responses[2] = response;
// })
// .catch(function(error){
//     console.log(error);
// });

// var r4 = axios.get(url[3])
// .then(function(response){
//     responses[3] = response;
// })
// .catch(function(error){
//     console.log(error);
// });

// var r5 = axios.get(url[4])
// .then(function(response){
//     responses[4] = response;
// })
// .catch(function(error){
//     console.log(error);
// });

// Promise.all([r1, r2, r3, r4, r5]).then(function(values){
//     console.log("Inside Promise: " + responses.length);
// });

// console.log("Outside Promise: " + responses.length);

// catTwo("./myText.txt", "./myTextTwo.txt", "./myTextThree.txt");

function saveWebPage(url, filename){

    rp(url).then(function(html){
        return html;
    })
    .then(function(html){
        
        fs.outputFile(filename, html, function(error){
            console.log(error);
        });

    })
    .catch(function(error){
        console.log(error);
    });

}

// function catTwo(inputOne, inputTwo, output){

//     var p1 = new Promise(function(resolve, reject){

//         fs.readFile(inputOne, 'utf8', function(err, data){

//             if (err) {
//                 reject(err);
//             } else {
//                 resolve(data);
//             }
    
//         });
//     });

//     var p2 = new Promise(function(resolve, reject){

//         fs.readFile(inputTwo, 'utf8', function(err, data){

//             if (err) {
//                 reject(err);
//             } else {
//                 resolve(data);
//             }
    
//         });
//     });

//     Promise.all([p1, p2]).then(function(array){
//         fs.outputFile(output, array[0] + array[1], function(error){
//             console.log(error);
//         })
//     })
//     .catch(function(error){
//         console.log(error);
//     });

// }

function addNumbers(numOne, numTwo){
    
    var p1 = new Promise(function(resolve, reject){

        if (Number.isInteger(numOne) && Number.isInteger(numTwo)){
            resolve(numOne + numTwo);
        } else {
            reject('Error');
        }
    
    });

    return p1;
}

addNumbers(5, 7)
.then(function(data){
    console.log(data);
})
.catch(function(error){
    console.log(error);
});

addNumbers('a', 7)
.then(function(data){
    console.log(data);
})
.catch(function(error){
    console.log(error);
});