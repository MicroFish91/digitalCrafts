// function Person(name, email, phone) { 
//     this.name = name; 
//     this.email = email; 
//     this.phone = phone; 
// } 

// Person.prototype.greet = function(other) { 
//     console.log('Hello ' + other.name + ', I am ' + this.name + '!'); 
// };

// var sonny = new Person("Sonny", "sonny@hotmail.com", "483-485-4948");
// var jordan = new Person("Jordan", "jordan@aol.com", "495-586-3456");

// sonny.greet(jordan);
// jordan.greet(sonny);
// console.log(`Name: ${sonny.name}, Email: ${sonny.email}, Phone: ${sonny.phone}`);
// console.log(`Name: ${jordan.name}, Email: ${jordan.email}, Phone: ${jordan.phone}`);

// Card Constructor
class Card {
    constructor(point, suit){
        this.point = point;
        this.suit = suit;
    }
}

var myCard = new Card(5, "Diamonds");

console.log(`${myCard.point} of ${myCard.suit}`);

Card.prototype.getImageUrl = function (){
    return `images/${myCard.point}_of_${myCard.suit}.png`;
}

console.log(myCard.getImageUrl());

class Hand {
    constructor(){
        this.myHand = [];
    }

    addCard(card){
        if (card.point > 10) {
            this.myHand.push(10);
        } else {
            this.myHand.push(card.point);
        }
    }

    getPoints(){
        var points = 0;

        if ((this.myHand).length > 0) {
            (this.myHand).forEach(function(index){
                points += index;
            });
        }
        
        console.log(points + " Points");

    }
}

var myHand = new Hand();
myHand.addCard(new Card(5, 'diamonds'));
myHand.addCard(new Card(13, 'spades'));
myHand.getPoints();

// Deck Constructor

