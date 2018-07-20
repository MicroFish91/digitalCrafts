// // Challenge 1
// var n = 496;
// var numString = "";

// while (n != 1) {
//     // Even
//     if ((n % 2) == 0) {
//         n /= 2; n = n / 2
//         numString = numString + n + " ";
//     }
//     // Odd
//     else if ((n % 2) != 0) {
//         n = n * 3 + 1;
//         numString = numString + n + " ";
//     }
//     else {
//         console.log("How'd we get here?");
//         break;
//     }
// }

// console.log(numString);

// Challenge 2

// Returns True if Palindrome, False if not
// function palindrome(product) {
//     product = product.toString();
//     var palindrome1 = "";
//     var palindrome2 = "";

//     // Read string front to back
//     for (x = 0; x < (product.length); x++){
//         palindrome1 += product[x];
//     }

//     //Read string back to front
//     for(x = (product.length - 1); x >= 0; x--) {
//         palindrome2 += product[x];
//     }

//     if (palindrome1 == palindrome2) {
//         return true;
//     } else {
//         return false;
//     }
// }


// var product = 0;
// var largestNumber = 0;

// for(let x = 1; x <= 999; x++){
//     for(let y = 1; y <= 999; y++){
//         product = x * y;
//         if (largestNumber < product) {
//             if (palindrome(product)) {
//                 largestNumber = product;
//             }
//         }
//     }
// }

// console.log(largestNumber);


// Challenge 3

// Checks if number is evenly divisible from 1 - 20, returns boolean
function checkDivisible(number){
    
    var divisor = 20;
    var divCheck = false;
    
    while ((((number / divisor) % 2) == 0) && (divisor > 1)){

        if (divisor == 1) {
            divCheck = true;
        }
        divisor--;
    }

    return divCheck;
}

// var smallestNumber = 2520;

// while (!(checkDivisible(smallestNumber))){
//     smallestNumber++;
// }

console.log(checkDivisible(2520));

