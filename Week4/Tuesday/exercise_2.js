// Madlib Function
function madLib(name, subject){
    console.log(name + "'s favorite subject in school is " + subject + ".");
};

madLib("Matt", "math");

// Tip Calculator 1
function tipAmount(amount, service) {
    if (service == "good") {
        return amount * 0.2;
    } else if (service == "fair") {
        return amount * 0.15;
    } else if (service == "bad") {
        return amount * 0.1;
    }
};

console.log(tipAmount(100, "fair"));

// Tip Calculator 2
function totalAmount(amount, service) {
    if (service == "good") {
        return (amount * 1.2);
    } else if (service == "fair") {
        return (amount * 1.15);
    } else if (service == "bad") {
        return (amount * 1.1);
    }
};

// Print Numbers
function printNumbers(start, end){
    for (let x = start; x <= end; x++){
        console.log(x);
    }

    let x = start;

    while(x <= end){
        console.log(x);
        x++;
    }
};

printNumbers(1, 10);

// Print a Square
function printSquare(size){
    let a = "";
    // Height of Stars
    for(let x = 0; x < size; x++){
        // Width of Stars
        for(let y = 0; y < size; y++) {
            a+="*";
        }
        console.log(a);
        a="";
    }
};

printSquare(7);
console.log("----");


// Print a Box
function printBox(width, height){
    let a = "";
    // Height
    for(let x = 0; x < height; x++){

        //****************
        if ((x == 0) || (x == (height - 1))){
            
            // Width
            for(let y = 0; y < width; y++) {
                a+="*";
            }

        } 
        // *___________*
        else {

            // Width
            for(let y = 0; y < width; y++) {
                if ((y == 0) || (y == (width - 1))) {
                    a+="*";
                } else {
                    a+=" ";
                }
            }
        }
        console.log(a);
        a="";
    }
};

printBox(7, 6);

// Print a Banner
function printBanner(message){
    let a = "";

    for(x = 0; x < message.length + 4; x++){
        a += "*";
    }
    
    console.log(a);
    a = ""

    console.log("* " + message + " *");

    for(x = 0; x < message.length + 4; x++){
        a += "*";
    }

    console.log(a);

}

printBanner("Hello Digitalcrafts!");

// Leetspeak
function leetspeak(message){
    let x = 0;

    while (x < message.length){
        switch (message[x]){
            case "A":
                console.log("4");
                break;

            case "E":
                console.log("3");
                break;
            
            case "G":
                console.log("6");
                break;

            case "L":
                console.log("1");
                break;

            case "O":
                console.log("0");
                break;
            
            case "S":
                console.log("5");
                break;

            case "T":
                console.log("7");
                break;

            default:
                console.log(message[x]);
                break;
        }
        x++;
    }
}

leetspeak("LEET");

// Long-long vowels
function longLongVowels(message){

    let y = "";

    for(x = 0; x < message.length; x++){
            
        if ((message[x] == "A") || (message[x] == "E") || (message[x] == "I") || (message[x] == "O") || (message[x] == "U")) {
            y+=message[x];
            y+=message[x];
            y+=message[x];
            y+=message[x];
            y+=message[x];
        } else {
            y+=message[x]
        }

    }

    console.log(y);
}

longLongVowels("CHEESE");

// Just the Positives
function positiveNumbers(numbers){
    let array = [];
    for(x = 0; x < numbers.length; x++) {
        if (numbers[x] >= 0) {
            array.push(numbers[x]);
        }
    }

    return array;
}

console.log(positiveNumbers([1, 5, -3, -7, 2, -9, 10, -11, 11]))