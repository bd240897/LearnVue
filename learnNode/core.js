// work with promise

// const promise = new Promise((resolve, reject) => {
//     resolve({a:10});
// }).then((x)=>{console.log(x); return x}).then((x)=>console.log(x))
//
// // function
// const some_function = function (username = 1, password = 1) {
//     return new Promise(function (resolve, reject) {
//         resolve("Stuff worked!");
//     });
// };

// some_function().then((x)=>{console.log(x); return x})

// promise from promie

// const first = function (x) {
//     return new Promise(function (resolve, reject) {
//         resolve(x*2);
//     });
// };
//
// const second = function (x) {
//     return new Promise(function (resolve, reject) {
//         resolve(x+1);
//     });
// };

// first(2)
//     .then((y)=>second(y))
//     .then((z)=>{console.log(z); return z})
//     .finally(()=>console.log('finally'))

// async promise

const first2 = async function (x) {
    return await new Promise(function (resolve, reject) {
        resolve(x*2);
    });
};

const second2 = async function (x) {
    return await new Promise(function (resolve, reject) {
        resolve(x+1);
    });
};

const three = async function () {
    const a = await first2(3).then((x)=>second2(x))
    const b = await second2(2)
    console.log(a)
    console.log(b)
}

three()