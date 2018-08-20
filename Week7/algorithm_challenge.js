var myArray = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5];

console.log(sumZeroCount(myArray));

function sumZeroCount (myArray){

    count = 0;

    for(let numOne = 0; numOne < myArray.length; numOne++){
        for(let numTwo = numOne + 1; numTwo < myArray.length; numTwo++){
    
            if (myArray[numOne] + myArray[numTwo] == 0){
                count++;
            }
    
        }
    }

    return count;

}

