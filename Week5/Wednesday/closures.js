function counter(number){

    var operation = {
        increment: function(){
            number++;
            console.log(number);
        },

        decrement: function(){
            number--;
            console.log(number);
        }
    }

    return operation;
}

var num1 = counter(5);
var num2 = counter(8);

num1.increment();
num2.decrement();

