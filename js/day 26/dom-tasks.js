// example 1
// let background_color = document.getElementById('background-color')

// background_color.addEventListener('click',function(){
//     // console.log('clicked')
//     background_color.style.backgroundColor = 'red'
// })

// let background_color_reset = document.getElementById('background-color-reset')

// background_color_reset.addEventListener('click',function () {
//     background_color.style.backgroundColor = 'white'

// })

// example 2

// let background_color = document.getElementById('background-color')

// background_color.addEventListener('click',function(){
//     // console.log('clicked')
//     let current_bg = background_color.style.backgroundColor

//     if(current_bg == 'red'){
//         background_color.style.backgroundColor = 'white'
//     } else {
//         background_color.style.backgroundColor = 'red'
//     }

// })

// task 2
let counter_btn = document.getElementById('counter-btn')
counter_btn.addEventListener('click',function() {

    let counter_span = document.getElementById('counter')
    let counter_value = counter_span.innerText
    
    counter_value++
    // counter_value = counter_value + 1; 

    counter_span.innerText = counter_value
    // console.log(counter_value)
    // console.log('clicked')
})

// task 3
let items = document.getElementsByClassName('items')

for(let i=0; i<items.length; i++  ){
    items[i].addEventListener('click',function(){
        items[i].style.display = 'none'
    })
    // console.log(items[i])
}

// task 4

let img_btn = document.getElementById('img-btn')
img_btn.addEventListener('click',function(){
    let img = document.getElementById('img')

    let current_h = img.style.height
    console.log(current_h)
    if(current_h == '500px'){
        img.style.height = '50px'
        img.style.width = '50px'
        img_btn.innerText = 'Cick to Enlarge'

    } else {
        img.style.height = '500px'
        img.style.width = '500px'
        img_btn.innerText = 'Cick to shrink'


    }
})

// taks 5
let color_btn = document.getElementById('form')

// console.log(color_btn)
form.addEventListener('submit',function(e) {
    e.preventDefault();
    let color = document.getElementById('color').value

    let body = document.querySelector('body')
    body.style.backgroundColor = color
})

// task 6
let input_count = 2
let new_btn = document.getElementById('new_btn')
new_btn.addEventListener('click',function(){
    let new_input = document.createElement('input')
    let br_elemment = document.createElement('br')
    new_input.name = 'input-'+input_count
    new_input.placeholder = 'input-'+input_count
    input_count++

    let inputs = document.getElementById('inputs')
    inputs.append(br_elemment)

    inputs.append(new_input)
});



// task 7

let fun_btn = document.getElementById('fun')
let fun_facts = [
    'Canada is south of Detroit (just look at a map).',
    'Bats are the only mammal that can actually fly.',
    'Elephants can’t jump',
    'Cows don’t actually have four stomachs; they have one stomach with four compartments.',
    'The platypus doesn\'t have a stomach at all: Their esophagus goes straight to their intestines',
    'Tigers’ skin is actually striped, just like their fur. Also, no two fur patterns are alike.'
]

fun_btn.addEventListener('click',function() {

    random_index = Math.floor( Math.random()*fun_facts.length )
    alert(fun_facts[random_index])
})

// task 8

let lucky_draw = document.getElementById('lucky_draw')

let participents = [
    'Ahmad',
    'Ali',
    'Abdullah',
    'Zahid',
    'Taha',
    'Abbas',
]

lucky_draw.addEventListener('click',function() {

    random_index = Math.floor( Math.random()*participents.length )
    alert('Congrats : ' + participents[random_index] + ' You are Winner !!!! ')
})