// Challenge Website: CodeWars
// Challenge Link: https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/javascript
// Challenge Description: It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

// My initial solution
function removeChar(str){
    return str.split("").slice(1, str.length - 1).join("");
  };

// Best solution presented
    // function removeChar(str) {
    //     return str.slice(1, -1);
    //   }

// 2nd best solution presented
    // const removeChar = str => str.slice(1,-1)

// 3rd best solution (long-hand)
    // function removeChar(str){
    //     return str.substring(1, str.length-1);
    //    };


// ------------------ SAMPLE TEST ------------------ 

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("Fixed Tests", () => {
    assert.strictEqual(removeChar('eloquent'), 'loquen');
    assert.strictEqual(removeChar('country'), 'ountr');
    assert.strictEqual(removeChar('person'), 'erso');
    assert.strictEqual(removeChar('place'), 'lac');
    assert.strictEqual(removeChar('ooopsss'), 'oopss');
  });
});