// console.log( document.getElementById('heading') )

// get any element using id
let heading = document.getElementById('heading')
console.log(heading)

// get any element using class name
let class_heading = document.getElementsByClassName('heading')
console.log(class_heading)

// get any element using tag name

let paragraph = document.getElementsByTagName('p')
console.log(paragraph)

// get any element using id or class or tag name

let query_id = document.querySelector(' #heading')
let query_class = document.querySelector(' .heading')
let query_tag = document.querySelector('p')

// get all element using id or class or tag name

let q_all_id = document.querySelectorAll('#heading')
let q_all_class = document.querySelectorAll('.heading')
let q_all_tag = document.querySelectorAll('p')

console.log(query_tag)
console.log(q_all_tag)

// get value/innerText content of any tag
let heading1 = document.getElementById('heading').innerText

let heading2 = document.getElementById('heading')
let inner_heading = heading2.innerText

console.log(heading1)
console.log(inner_heading)


//get content with html tags of any element
let div_element = document.getElementsByTagName('div')
// let div_element = document.getElementById('div')
let inner_text = div_element[0].innerText
// let inner_text = div_element[0].innerHTML

console.log(div_element)
console.log(inner_text)





