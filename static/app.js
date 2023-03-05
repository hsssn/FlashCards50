const termdata = document.querySelector('#passingdiv');
const term = document.querySelector('#termm');
const meaning = document.querySelector('#meaning');
const next = document.querySelector('#next');                   
termJson = JSON.parse(termdata.innerHTML);


next.addEventListener ('click', function(){
  var random = Math.floor(Math.random() * Object.keys(termJson).length);
  term.style.display = 'block';
  term.innerHTML = termJson[random]["word"];
  meaning.style.display = 'block'
  meaning.innerHTML = termJson[random]["meaning"];
});
