let today = new Date();

let year = today.getFullYear();
let month = String(today.getMonth() + 1).padStart(2, '0');
let date = String(today.getDate()).padStart(2, '0');

console.log(`${year}-${month}-${date}`)