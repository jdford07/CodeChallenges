// Challenge Website: CodeWars
// Challenge Link: https://www.codewars.com/kata/56dec885c54a926dcd001095/train/javascript
// Challenge Description: Very simple, given an integer or a floating-point number, find its opposite.


// My initial solution
function opposite(number) {
    return number%2 ? -number : Math.abs(number)
  }

// Best solution presented
    // function opposite(number) {
    //     return(-number);
    //   }

// 2nd best solution presented
  //const opposite = number => -number;

// 3rd best solution (long-hand)
    // function opposite(number) {
    //     return number * (-1);
    // }


// ------------------ SAMPLE TEST ------------------ 
