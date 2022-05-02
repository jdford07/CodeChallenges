// Challenge Website: CodeWars
// Challenge Link: https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/javascript
// Challenge Description: Your task is to create a function that does four basic mathematical operations.The function should take three arguments - operation(string/char), value1(number), value2(number). The function should return result of numbers after applying the chosen operation.

// My initial solution
// Best solution
function basicOp(operation, value1, value2)
{
  //Using eval is a security risk, therefor, will not use
  switch(operation) {
    case '+': return value1 + value2;
    case '-': return value1 - value2;
    case '*': return value1 * value2;
    case '/': return value1 / value2;
    default: return 0;
  }
}

// Interesting variation
    // function basicOp(operation, value1, value2)
    // {
        // var cases = {
        //     '+': value1 + value2,
        //     '-': value1 - value2,
        //     '*': value1 * value2,
        //     '/': value1 / value2
        // };
        // return cases[operation]
    // }

// ------------------ SAMPLE TEST ------------------ 
describe("Tests", () => {
    it("test", () => {
  console.log("Basic tests\n");
  Test.assertSimilar(basicOp('+', 4, 7), 11);
  Test.assertSimilar(basicOp('-', 15, 18), -3);
  Test.assertSimilar(basicOp('*', 5, 5), 25);
  Test.assertSimilar(basicOp('/', 49, 7), 7);
    });
  });
  