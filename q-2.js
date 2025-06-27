
let car={
    brand:'porche',
    model:911,
    year:2018,
    color:'white',
}
let arr1=[]
 for(key in car){
        arr1.push(key,arr1[key])
    }
console.log(arr1);
let value=''
for(Elemen of arr1){
    value+=Elemen
}
console.log(value);

let carob={
    brand:'porche',
    model:911,
    year:2018,
    color:'white',
}
function about(obj){
    let arr=[]
    for(key in obj){
        arr.push(key,obj[key])
    }
    return arr.toString()
}
console.log(about(carob));

