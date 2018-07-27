// Challenge 1
// Pass a number to determine if a prime number, returns a boolean
function isPrime(number){

    for(let x = 2; x < number; x++){
        if (number % x == 0) {
            return false;
        }
    }

    return true;
}

// Creates primes through a beginning and end limit
function createPrimes(start, end){

    var array = [];

    for(let x = start; x <= end; x++){
        if (isPrime(x)){
            array.push(x);
        }
    }

    return array;

}

// Store into composite primes
function findPrimes(number){

    let array = [];

    for (let index = 0; index <= number; index++) {
        if(primes[index] < number){
            array.push(primes[index]);
        } else {
            return array;
        }
    }
}

// Highest Square to test to
function squareLimit (number){
    var square = Math.ceil(Math.sqrt(number));
    return square;
}

function equationCheck(number){

    compositePrimes = findPrimes(number);
    
    for(var primeIndex = 0; primeIndex < compositePrimes.length; primeIndex++){
        for(var square = 1; square <= squareLimit(number); square++){
            if (number == (compositePrimes[primeIndex] + 2 * (square * square))) {
                return true;
            }
        }  
    }

    return false;

}

function oddComposite(number){
    if (!isPrime(number) && !(number % 2 == 0)){
        return true;
    } else {
        return false;
    }
}


// Main
var primes = [];
var compositePrimes = [];
var number = 3;
var check = true;

primes = createPrimes(2, 10000);

while (check){
    if (oddComposite(number)){
        if (!equationCheck(number)){
            check = false;
        }
    }
    
    number+=2;
}

console.log(number-=2);



// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------




// // Challenge 2
// var beerOne = 99;
// var beerTwo = 98;
// var swap = true;

// while ((beerOne > 0) && (beerTwo > 0)){
    
//     if (swap){
//         beerOne -= 2;
//         swap = false;

//         console.log(`${beerTwo} bottles of ${beer(beerTwo)}, take one down, pass it around, ${beerOne} bottles of ${beer(beerOne)} on the wall.`);

//     } else {
//         beerTwo -= 2;
//         swap = true;

//         console.log(`${beerOne} bottles of ${beer(beerOne)}, take one down, pass it around, ${beerTwo} bottles of ${beer(beerTwo)} on the wall.`);
//     }

// }

// function beer(number){

//     if ((number % 7 == 0) && (number % 5 == 0)) {

//         return "Miller Lite";

//     } else if ((number % 5) == 0) {
        
//         return "Lite beer";
    
//     } else if ((number % 7) == 0) {

//         return "Miller";

//     }

//     return "beer";
// }




// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------
// -------------------------------------------------------------------------------


// // Challenge 3

// var cakeTypes = [
//     {weight: 7, value: 160},
//     {weight: 3, value: 90},
//     {weight: 2, value: 15},
// ];

// var capacity = 20;

// console.log(maxDuffelBagValue(cakeTypes, capacity));

// // By Efficiency
// function maxDuffelBagValue(cakeType, capacity){

//     cakeType.sort(function(a, b){
//         return (b.value / b.weight) - (a.value / a.weight);
//     });

//     var maxValue = 0;
//     var cakeNumber = 0;

//     for(let index = 0; index < cakeType.length; index++){
//         if ((capacity / cakeType[index].weight) >= 1) {
            
//             cakeNumber = Math.floor((capacity / cakeType[index].weight));
//             capacity -= (cakeNumber * cakeType[index].weight);
//             maxValue += (cakeNumber * cakeType[index].value);
//         }
//     }
//     return maxValue;
// }


