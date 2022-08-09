// To verify wheather JS is executing or not?
console.log('JavaScript Executed Successfully!!!');

// If there is nothing in the table keep it be and try not to show the table data
const todos = document.getElementById('todo');
console.log(todos.row.length)
function show(){
    if (todos.row.length == 0){
        todos.style.display='none'
    }
    else{
        todos.style.display='block'
    }
}