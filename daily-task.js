let arr=[5,6,7,8,9]

function avrage(...num){
    let result=0
    for(number of num){
        result+=number
    }return result
}

console.log(avrage(1,2,3,4,...arr));
let antarr=[10,11,12,13]
let merge=[...arr,...antarr]
console.log(merge);