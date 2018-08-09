function add(x, y, callback) {
    var result = x + y; 
    callback(result); 
 } 
 
 function subtract(x, y, callback) { 
    var result = x - y; 
    callback(result);
 } 
 
 function greeting(person, callback) { 
    var result = 'Hola, ' + person + '!'; 
    callback(result);
 } 
 
 function product(numbers, callback) { 
    var result = numbers.reduce(function(a, b) { 
       return a * b; 
    }, 1); 
    callback(result);
 }

 function log(message){
     console.log(message);
 }

 var myArray = [1, 2, 3, 4, 5];

 product(myArray, log);
 add(myArray[0], myArray[1], log);
 greeting("Matt", log);
 subtract(myArray[2], myArray[1], log);

