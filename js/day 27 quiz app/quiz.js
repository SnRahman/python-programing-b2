
// make array of questions
let questions = [
    {
        'title' : 'What is 10 / 2?',
        'options' : [10,25,36,5],
        'answer' : 5
    },
    {
        'title' : 'What is 15 - 10?',
        'options' : [10,5,36,12],
        'answer' : 5
    },
    {
        'title' : 'What is 4 + 10?',
        'options' : [10,14,36,12],
        'answer' : 14
    },
    {
        'title' : 'What is the capital of Pakistan?',
        'options' : ['Lahore','Islamabad','Faisalabad','Multan'],
        'answer' : 'Islamabad'
    },

]

// initialise variables
let questions_index = 0
let result = 0

// function to start the game on start button click
function start() {
    questions_index = 0
    result = 0
    let start_btn = document.getElementById('start')
    start_btn.addEventListener('click',function() {
        add_question()
    })
}

// call the start function
start()


// function for displaying new question on the screen every time
function add_question() {
    let current_question = questions[questions_index]
    console.log(current_question)

    let container = document.getElementById('container')
    container.innerHTML = '<h1>' + current_question.title +'</h1>'

    for(option of current_question.options ) {
        let option_btn_new = document.createElement('button')
        option_btn_new.innerText = option
        container.append(option_btn_new)
    }
    
    check_answer()
}

// function for evaluating the user option seletion and then displaying the next question
function check_answer() {
    let current_question = questions[questions_index]
    let option_btns = document.querySelectorAll('button')

    for(option_btn of option_btns){
        option_btn.addEventListener('click',function() {

            // get the value of button on which user clicked
            let user_selection = this.innerText

            // check if user selection is matched with the correct answer
            if(user_selection == current_question.answer){
                result++
            }

            //place check weither diplay new question of end the game if question finished.
            if(questions_index < questions.length  - 1)
            {
                questions_index++
                add_question()
            }
            else{
                end_game()
                // console.log('game over ')
            }

        });
    }
}

// function of creating end game elements
function end_game(){
    let container = document.getElementById('container')
    container.innerHTML = '<h1> Game Over ! </h1> <h1> Score: ' + result + '/' + questions.length + '</h1>'

    let restart_btn = document.createElement('button')
    restart_btn.id = 'start'
    restart_btn.innerText = 'Restart'

    container.append(restart_btn)
    start()
}