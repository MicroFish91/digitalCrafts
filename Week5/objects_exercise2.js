// var mom = { 
//     firstName: 'Alice', 
//     lastName: 'Wong', 
//     eyeColor: 'brown', 
//     hairColor: 'black' 
// }; 

// var daughter = { 
//     firstName: 'Ilene', 
//     hairColor: 'brown' 
// };

class Person{
    constructor(name){
        this.name = name;
        this.friends = [];
        this.greetings = [];
    }

    addFriend(friend){
        this.friends.push(friend);
    }

    createGreeting(other){
        this.greetings.push('Yo ' + other.name + '! from ' + this.name + '.');
        return 'Yo ' + other.name + '! from ' + this.name + '.';
    }

    greet(other){
        console.log(this.createGreeting(other)); 
    }

    lazyGreet(other){
        setTimeout(() => (this.greet(other)), 2000);
    }

    createGreetingsForFriends(){
        return this.greetings.map(function(index){
            return index;
        });
    }

}


// These thises
var someone = new Person("Matt");
var joe = new Person("Joe");
someone.lazyGreet(joe);

// These Thises 2
someone.createGreeting(joe);
console.log(someone.createGreetingsForFriends());