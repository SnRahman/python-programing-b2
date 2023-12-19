let form = document.getElementById('form')

// get todos form localstorage
let current_todos = localStorage.getItem('todo_list')

let todo_list = document.getElementById('todo_list')
todo_list.innerHTML = current_todos

// console.log(current_todos)

form.addEventListener('submit',function(e){
    e.preventDefault()

    // get new todo value from input
    let new_todo_item = document.getElementById('todo').value
    if(new_todo_item == ''){
        alert('Please Enter a valid task.`')
    }else{
        // create new li element
        let new_li = document.createElement('li')
        new_li.classList.add('todo-item')
        new_li.innerHTML = '<span>'+new_todo_item +'</span> <button type="button" id="delete_btn">X</button>'

        // append li in ul tag
        let todo_list = document.getElementById('todo_list')
        todo_list.append(new_li)

        //save list in local storage 
        add_todo()
        li_events()
    }
})

function li_events(){
    // get all lis for loop
    let lis = document.querySelectorAll('.todo-item')
    for(li in lis){
    
        // let span = li.children[0]
        // span.addEventListener(){
        // }

        let list = lis[li]

        // console.log(list.children[0])
        list.children[0].addEventListener('click',function(){
            // this.classList.toggle('marked')
            this.classList.add('marked')
            add_todo()
        })

        list.children[1].addEventListener('click',function(){
            list.remove()
            add_todo()
        })
    }
}
function add_todo(){
    //save list in local storage 
    let list = document.getElementById('todo_list').innerHTML
    localStorage.setItem('todo_list',list)
}


li_events()

// console.log(lis)
