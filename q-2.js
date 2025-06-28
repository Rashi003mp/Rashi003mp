/*
let arr1=[1, 2, 3, 4]
let sum=arr1.reduce((accu,index)=>accu+index)
console.log(sum);

let arr=[1, 2, 3, 4]
let mut=arr.reduce((accu,index)=>accu*index)
console.log(mut)



let fruits=['apple', 'banaaana', 'kiwi']
let longestword=fruits.reduce((accum,index)=>index.length>accum.length?index:accum)
console.log(longestword);*/

// const numbers = [10, 25, 3, 8];
// const max=numbers.reduce((accu,index)=>index>accu?index:accu)
// console.log(max);
// const numbers = ['cat', 'dog'];
// // const max=numbers.reduce((accu,index)=>{accu[index]=index.length; return accu} )
// // console.log(max);

// let a=numbers.map(numbers)
// let b=numbers.forEach()
// console.log(a);
// console.log(b);


// function fizzBuzz  (n) {
//     let result = []
//     for (let i = 1; i <= n; i++) {
//         if (i % 3 === 0 && i % 5 === 0) {
//             result.push('fizzBuzz')
//         } else if (i % 3 === 0) {
//             result.push('fizz')
//         } else if (i % 5 === 0) {
//             result.push('Buzz')
//             } else {
//     result.push (i.toString())     
//         }
//     } return result
// };
// console.log(fizzBuzz(15));

// var fizzBuzz = function(n) {
//   let result = [];

//   for (let i = 1; i <= n; i++) {
//     let str = "";

//    // if (i % 3 === 0&&i % 5 === 0) str += "Fizzbuzz";
//     if (i % 3 === 0) str += "Fizz";
//     if (i % 5 === 0) str += "Buzz";

//     result.push(str || i.toString());
//   }

//   return result;
// };
// console.log(fizzBuzz(15));

// function factorial (num){

//   if (num<=1)
//     {return 1}
//   return num*factorial(num-1)
    
// }

// let a=factorial(5)
// console.log(a);




// Lexical scope means:

// A function can use variables from the place it was written, even if it's called somewhere else.
//  Imagine this:
// Think of your code like a house.

// Each room is a function.

// If a function is written inside another function, it can see the things in the outer room.

// function rsuse(...numbers){
//   let res=0
//   for(let num of numbers){
//     res+=num
//   }
//   return res
// }
// console.log(rsuse(5));

// function findmax(...a){
//   let result=0
//   for(number of a){
//     result+=number
//   }
//   return result
// }
// console.log(findmax(5,6,1));


// function joinword(...word){
//   let res=''
//   for(words of word){
//     res+=words+' '
//   }
//   return res
// }
// console.log(joinword('latin','america','is notusa'));

let numbers = [1, 2, 3, 4];
// let copy = [...numbers]
// let mergedArr = [...numbers, ...copy]
//let person = { name: "Rashi", age: 20 };
// let copyobj={...person}
// console.log(mergedArr);
// console.log(copyobj);


// let add={...person, subject:'maths'}
// let mergr={...person,...add}
// console.log(add);
// console.log(mergr);

function add(a,...numbers){
  return a+' ,'+ numbers
}
console.log(add(1,numbers));
let nested = [1, [2, 3], 4];
let falttern=[...nested]
console.log(falttern);


