const termdata = document.querySelector('#passingdiv');
const check = document.querySelector('#submm');
const nextquiz = document.querySelector('#nextt');
const quizterm = document.querySelector('#quizterm');
const quizcorrect = document.querySelector('#quizcorrect');  
const userAnswer = document.querySelector('#quizmeaning');
const start = document.querySelector('#start');                   
termJson = JSON.parse(termdata.innerHTML);


nextquiz.addEventListener ('click', function(){
  var random = Math.floor(Math.random() * Object.keys(termJson).length);
  quizterm.innerHTML = termJson[random]["word"];
  quizcorrect.innerHTML = termJson[random]["meaning"];
  document.querySelector('#feedback2').style.display = "none";
});


check.addEventListener('click', function() {
  if (userAnswer.value == quizcorrect.innerHTML){
    document.querySelector('#feedback2').style.display = 'block';
    document.querySelector('#feedback2').innerHTML = 'Correct!';
  }
  else {
    document.querySelector('#feedback2').style.display = 'block';
    document.querySelector('#feedback2').innerHTML = 'Inorrect!';
  }
}
)

