let click = document.getElementById('click')

// method 1 using anonymeous function
// console.log(click)
click.addEventListener('click', function () {
    alert("Hello World")
} )



// method 2 using genral function
let click_function = document.getElementById('click-function')
click_function.addEventListener('click', display)


function display(){
    alert("Hello World function")
}

// on mouse over event
let mover_over = document.getElementById('mouseover')
mover_over.addEventListener('mouseover',function(){
    // alert('Mouse over Event')
    console.log('Mouse over Event')
})


// on mouse out event

let mouse_out = document.getElementById('mouseout')

mouse_out.addEventListener('mouseout',function (){
    console.log('Move out Event')
})

// on foucus event on input


let focus = document.getElementById('focus')

focus.addEventListener('focus',function () {
    console.log('input is focused')
})

// on blur event on input

let blur = document.getElementById('blur')
blur.addEventListener('blur',function () {
    console.log('input is out of focus.')
})

// add menucontext event
let menu = document.getElementById('menu')
menu.addEventListener('contextmenu',function (e) {
    console.log('context menu function')
    e.preventDefault()
})

// submit form event

let form = document.getElementById('form')

form.addEventListener('submit',(event) => {
    event.preventDefault()
    console.log('form is submitted')
})

// multiple events on single element

let multiple = document.getElementById('multiple')

multiple.addEventListener('click', () => {
    console.log('multiple evnets button clicked')
})

multiple.addEventListener('mouseover', () => {
    console.log('multiple evnets button is mouse over')
})

multiple.addEventListener('mouseout', () => {
    console.log('multiple evnets button is mouse out')
})


let multiple_input = document.getElementById('multiple_input')
multiple_input.addEventListener('focus', () => {
    console.log('input is focused')
})

multiple_input.addEventListener('blur', () => {
    console.log('input is out of focused')
})

// execute an event once

let once = document.getElementById('once')

once.addEventListener('click',display_once)

function display_once(){
    console.log('Event will be executed once.')

    once.removeEventListener('click',display_once)
}

// parent child example

let inner_btn =  document.getElementById('inner-btn')
let inner_div =  document.getElementById('inner-div')
let outer_div =  document.getElementById('outer-div')


outer_div.addEventListener('click',function() {
    console.log('outer div is clicked (capturing)')
},true)


inner_div.addEventListener('click',function(e) {
    console.log('inner div is clicked (capturing)')
    e.stopPropagation()
},true)  




inner_btn.addEventListener('click',function(e){
    console.log('inner btn is clicked')
    // e.stopPropagation()
})

inner_div.addEventListener('click',function(){
        console.log('inner div is clicked (bubbling)')
    })

outer_div.addEventListener('click',function(){
    console.log('outer div is clicked (bubbling)')
})
