// Positive Numbers
var posArray = [1, 3, -5, 12, 7, -9, -14];

var newArray = posArray.filter(function(index){
    return index > 0;

});

console.log(newArray);

// Even Numbers
var newArray = posArray.filter(function(index){
    return ((index % 2) == 0);

});

console.log(newArray);

// Square the Numbers
var newArray = posArray.map(function(index){
    return index * index;

});

console.log(newArray);

// Cities 1
var cities = [ { name: 'Los Angeles', temperature: 60.0}, { name: 'Atlanta', temperature: 52.0 }, { name: 'Detroit', temperature: 48.0 }, { name: 'New York', temperature: 80.0 } ];

var lowerCities = cities.filter(function(index){
    return index["temperature"] < 70;
});

console.log(lowerCities);

// Cities 2
var newCities = cities.map(function(index){
    return index["name"];

});

console.log(newCities);

// Good Job!
var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ];

people.forEach(function(index){
    console.log("Good job " + index + ".");
});

// Sort an Array Alphabetically
console.log(people.sort());

// Sort Array by String Length
console.log(people.sort(function(a, b){
    return a.length - b.length;
}));

// Sort by Sum
var arr = [ [1, 3, 4], [2, 4, 6, 8], [3, 6] ];

var sortedArray = arr.sort(function(a, b){
    
    var sum1 = 0;
    var sum2 = 0;
    var iteration1 = 0;
    var iteration2 = 0;
    var first = 0;
    var second = 0;
    
    a.forEach(function(index){
        sum1+=index;

        if (iteration1 == (a.length-1)) {
            first = sum1;
            iteration1 = 0;
        }

        iteration1++;

    });
    
    b.forEach(function(index){
        sum2+=index;

        if(iteration2 == (b.length-1)) {
            second = sum2;
            iteration2 = 0;
        }
        iteration2++;
    });

    return first - second;

});

console.log(sortedArray);

// 3 times
function call3Times(fun) { fun(); fun(); fun(); }

function fun(){
    console.log("Hello World!");
};

call3Times(fun);
console.log("-------");

// n times
function callNTimes(number, fun) { 
    for(x = 0; x < number; x++){
        fun();
    }
}

callNTimes(5, fun);


// Sum an Array
var array = [1, 3, 4, 6];

function sum(array){
    sum = 0;

    array.forEach(function(index){
        sum+=index;
    });

    console.log(sum);
};

sum([1, 2, 4]);

// Acronym
var words = ["very", "important", "person"];
var acronym = words.map(function(index){
    return index[0];
});

console.log(acronym.join(""));