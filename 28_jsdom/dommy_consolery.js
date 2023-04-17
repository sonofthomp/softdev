// Team Greatness-Portending Team :: Jun Hong Wang, Gabriel Thompson 
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

//takes a text argument and creates a new item at end of list
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

//takes index argument
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

//makes all uncolored items red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

//stripes uncolored items, alternating between red and blue
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FAC
var fact = function(n) {
  if (n < 2) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
// FIB
var fib = function(n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }
}
// GCD
var gcd = function(a, b) {
  var c = 0;
  if (a == b) {
    return a;
  } else if (a < b) {
    for (let i = 0; i <= a; i++) {
      if (a % i == 0 && b % i == 0) {
        c = i;
      }
    }
    return c;
  } else {
    for (let i = 0; i <= b; i++) {
      if (a % i == 0 && b % i == 0) {
        c = i;
      }
    }
    return c;
  }
}

//test calls
console.log(fact(5));
console.log(fib(5));
console.log(gcd(5,5));
console.log(gcd(20,24));
console.log(gcd(24,20));
console.log(gcd(3,9));

//thing to make function call on page load
var load = function() {
  addItem("5! is " + fact(5));
  addItem("the 6th fib number is " + fib(6));
  addItem("the gcd of 20 and 24 is " + gcd(20,24));
}

load();

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const bobby = (x, y) => {
  // body
  retVal = 3 + x - 2 * y;
  return retVal;
};

//more test calls
console.log(bobby(3,7));
console.log(bobby(1,1));
console.log(bobby(5,4));