<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>
</head>
<body>
    <form>
        <input type="text" id="task">
    <input type="submit">
    </form>
    
    <script src="script.js"></script>
</body>
</html>



// localStorage.setItem('name','Shreyas');
// sessionStorage.setItem('name','Hello');

const name = localStorage.getItem('name');
console.log(name)
// localStorage.clear()

document.querySelector('form').addEventListener('submit',function(e){
    const task = document.querySelector('#task').value;

    let tasks;
    if(localStorage.getItem('task')===null){
        tasks = [];
    }else{
        tasks = localStorage.getItem('tasks')
    }
    tasks.push(task)
    document.write(tasks)
    localStorage.setItem('tasks',JSON.stringify(tasks));

})
