function generateRandomLexicalUppercaseEnglishCharacters(n) {
  const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let result = "";
  for (let i = 0; i < n; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}
function generateRandomNumbers(n, min, max) {
  let result = [];
  for (let i = 0; i < n; i++) {
    result.push(Math.floor(Math.random() * (max - min + 1)) + min);
  }
  return result;
}

console.log(
  `"lexical_arr": [${generateRandomLexicalUppercaseEnglishCharacters(10)
    .split("")
    .map((e) => `"${e}"`)}],`
);
console.log(`"numerical_arr": [${generateRandomNumbers(10, 0, 150)}],`);
