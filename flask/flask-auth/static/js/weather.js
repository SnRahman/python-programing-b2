let form = document.getElementById('form')
const kelvin_const = 273.15

const api_key = '3d94d884787c276b1107b5e5cac522ab'
form.addEventListener('submit',async function(e){
    e.preventDefault()

    let city_name = document.getElementById('city_name').value
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${api_key}`

    if(city_name == ''){
        alert('Kindly enter a valid city name')
    } else {
        let response = await fetch(url)

        let data = await response.json()

        // data
        get_date(data)
        get_loc(data)
        get_temp(data)    
        get_feels_like_temp(data)
        get_humidity(data)
        get_pressure(data)
        console.log(response)
        // console.log(city_name)
        console.log(url)
    }
})


function get_date(data){
    const months_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    let date_dt = data.dt * 1000
    let date = new Date(date_dt)

    let month_index = date.getMonth()
    let month = months_short[month_index]

    let current_date = date.getDate()
    let minutes = date.getMinutes()
    let hours = date.getHours()

    let ampm = ''

    if(hours>=12){
        ampm = 'PM'
    } else {
        ampm ='AM'
    }

    let final_date = `${month} ${current_date}, ${hours}:${minutes}${ampm} `

    let date_element = document.getElementById('date')
    date_element.innerText = final_date

    // console.log(final_date)
    // console.log(ampm)
    // console.log(minutes)
    // console.log(hours)
    // console.log(current_date)
    // console.log(month)
    // console.log(month_index)
    // console.log(date)
}

function get_loc(data){
    let city = data.name
    let country = data.sys.country

    let final_loc = `${city}, ${country}`

    let loc_element = document.getElementById('loc')
    loc_element.innerText = final_loc
}

function get_temp(data) {
    const kelvin_const = 273.15
    let temp = data.main.temp
    let temp_in_c = temp - kelvin_const
    temp_in_c =  temp_in_c.toFixed(0) 
    let final_temp = `${temp_in_c}&deg C`
    let temp_element = document.getElementById('temp')
    temp_element.innerHTML = final_temp
}



function get_feels_like_temp(data){
    let temp = data.main.feels_like
    let temp_in_c = temp - kelvin_const
    temp_in_c =  temp_in_c.toFixed(0)
    
    let weather = data.weather[0].main
    console.log(weather)
    let final_temp = `Feels Like ${temp_in_c}&deg C ${weather}`
    let feels_like_temp = document.getElementById('feels_like_temp')
    feels_like_temp.innerHTML = final_temp
}

function get_humidity(data) {
    let humidity = data.main.humidity
    let humidity_element = document.getElementById('humidity')
    humidity_element.innerText = humidity
}

function get_pressure(data) {
    let pressure = data.main.pressure
    let pressure_element = document.getElementById('pressure')
    pressure_element.innerText = pressure
}