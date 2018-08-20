var express = require('express');
var app = express();

// Set up server
app.listen(8000, function () {
    console.log('Listening on port 8000');
});

// Set up code for a url extension '/'
app.get('/', function(req, res){
    res.send("Hello World!");
});

// Set up code for a url extension '/cats'
app.get('/cats', function(req, res){
    res.send("Meow!");
});

// Set up code for a url extension '/dogs'
app.get('/dogs', function(req, res){
    res.send("Such dog. Much bark.");
});

// Set up code for a url extension '/cats_and_dogs'
app.get('/cats_and_dogs', function(req, res){
    res.send("Living together.");
});

// Greet User
app.get('/greet/:user', (req, res) => {
    
    var user = req.params.user;
    res.send(`Hello ${user}!`);

});

// Age
app.get('/year', (req, res) => {

    var date = new Date();
    var age = date.getFullYear() - req.query.age;
    
    res.send(`You were born in ${age}!`);

});

