function lvl6exercise1(num) {
	// Return 'hello' if num is 1, 'world' if num is 2, otherwise return'bye'
	if (num == 1) {
		return "hello";
	} else if (num == 2) {
		return "world";
	} else {
		return "bye";
	}
}

console.log(lvl6exercise1(1));
console.log(lvl6exercise1(2));
console.log(lvl6exercise1(3));

function lvl6exercise2() {
	// Push 10 "hello" strings into the array using a for loop, then return it
	var array = [];
	for (x = 0; x < 10; x++) {
		array.push("hello");
	}

	return array;
}

console.log(lvl6exercise2());

function lvl6exercise3() {
	// Empty this array using a while loop and return it
	var array = ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"];
	while (array.length > 0) {
		array.pop();
	}

	return array;
}

console.log(lvl6exercise3());


