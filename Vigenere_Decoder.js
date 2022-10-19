const {readFileSync} = require('fs');

const dictionary = readFileSync('./usa2.txt', 'utf-8').split(/\r?\n/);

const commandInput = process.argv.slice(2);
const cipherText = commandInput[0];
const keyLength = parseInt(commandInput[1]);

const findKeyPhrase = function(cipher, keyLen){
  let potentialMatches = [];
  let potentialKeys = [];

  for (let i = 0; i < dictionary.length; i++){
    if (dictionary[i].length === keyLen){
      potentialKeys.push(dictionary[i]);
    }
  }
  console.log('There are ' + potentialKeys.length + ' potential keys');

  let keyArray = [...Array(keyLen)].map(() => {
    return 0;
  });

  console.log('Searching for valid decriptions...')
  for (let x = 0; x < potentialKeys.length; x++){
    for (let y = 0; y < keyArray.length; y++){
      keyArray[y] = potentialKeys[x].charCodeAt(y) - 97;
    }
    let decoded = decodeCipher(cipher, keyArray);
    let validity = depthFirstWordSearch(decoded)
    if(validity){
      potentialMatches.push(decoded)
    }
  }
  console.log('There are ' + potentialMatches.length + ' potential match(es)');
  console.log(potentialMatches);
}

// takes cipher and key converted to a number array and returns plaintext
const decodeCipher = function(cipher, keyArr){
  let output = '';
  for (let i = 0; i < cipher.length; i++){
    let keyCode = cipher.charCodeAt(i) - keyArr[i % keyArr.length];
    if(keyCode < 97){
      keyCode += 26
    }
    output += (String.fromCharCode(keyCode));
  }
  return output
}

const depthFirstWordSearch = function (phrase, currentPosition=''){
  if(currentPosition === phrase){
    console.log('found a match!');
    return true;
  }
  for (let i = currentPosition.length + 1; i <= phrase.length; i++){
    let searchable = phrase.slice(currentPosition.length,i);
    const match = dictionary.find(el => {
      if (el === searchable){
        return true;
      }
    });
    if(match !== undefined){
      if (depthFirstWordSearch(phrase, phrase.slice(0, i))){
        return true;
      }
    }
    const startsWith = dictionary.find(el => {
      if(el.startsWith(searchable) && el !== searchable){
        return true;
      }
    });
    if (startsWith === undefined){
      break;
    }
  }
  return false;
}

findKeyPhrase(cipherText, keyLength);
