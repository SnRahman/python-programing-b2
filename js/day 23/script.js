
// add style to any element
// method 1
let p_style = document.getElementById('p_style')

p_style.style.color = '#059862'
p_style.style.backgroundColor = 'red'

// method 2
document.getElementById('p_style').style.color = 'red'
document.getElementById('p_style').style.backgroundColor = 'green'


// add new tag/element 

// create new element
let new_element = document.createElement('p')
new_element.innerText = 'Element created'

let new_element1 = document.createElement('h3')
new_element1.innerText = 'Heading created by js'

// add new created element(s) using append function
// document.getElementById('container').append(new_element,new_element1)
document.getElementById('container').append(new_element)

//append in element
// let container = document.getElementById('container')
// container.append(new_element)


// append just one element at a time

let new_element2 = document.createElement('u')
new_element2.innerText = 'Underline tag created by js'

document.getElementById('p_style').appendChild(new_element2)

// append new element at start of the tag/element

document.getElementById('container').prepend(new_element1)

// remove any tag from document 

// document.getElementById('remove').remove()

let item = document.getElementById('remove')
item.remove()

// get attribute 

let anchor = document.getElementById('anchor')
// method 1
// let href_value = anchor.getAttribute('href')
let href_value = anchor.href
// method 2
let target_value = anchor.getAttribute('target')

console.log(anchor)
console.log(href_value)
console.log(target_value)

// set attribute value

let heading = document.getElementById('heading')
heading.setAttribute('class','background')

heading.style.border = '1px solid black'

document.getElementById('div1').setAttribute('class','div-style')
document.getElementById('div1').style.border = '1px solid black'

//dataset

// get data set values 
let data_container = document.getElementById('data')
let email = data_container.dataset.email




// console.log(email)

//set dataset values
data_container.dataset.phone_no = '0300123456789 '

// dataset direct get and set values
console.log( document.getElementById('data').dataset.email )
document.getElementById('data').dataset.id = 32354564


let heading1 = document.getElementById('heading1')

// heading1.setAttribute('class','background')
// heading1.setAttribute('class','border')

heading1.classList.add('background')
heading1.classList.add('border')
// heading1.classList.add('size')


//remove any class
heading1.classList.remove('size')



// swtich the classes 
heading1.classList.toggle('size')
heading1.classList.toggle('size')



