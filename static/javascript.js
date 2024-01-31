const form = document.getElementById("formSubmit");
const listvalues = document.getElementById("list");




form.addEventListener('submit', (event) => {
    event.preventDefault();

const value1 = document.getElementById('name').value;
const value2 = document.getElementById('email').value;
const value3 = document.getElementById('elements').value;
const value4 = document.getElementById('comment').value;

const radiovalues = document.querySelectorAll('input[type="radio"]:checked');
const generalradiovalues = Array.from(radiovalues).map(input => `${input.name}: ${input.value}`).join(', ');


const textvalues = document.querySelector('textarea[name="text"]');
const generaltextvalues = textvalues ? `<b>Values:</b> ${textvalues.value}` : '';


const listedvalues = document.createElement('li');
listedvalues.innerHTML = 

`<b>Name:</b> ${value1}<br>
<b>Email:</b> ${value2}<br>
<b>Options:</b> ${value3}
<b>Ratings:</b> ${generalradiovalues} ${generaltextvalues}<br>
<b>Comment:</b> ${value4} <hr style="border: 1px solid black;">
`;




listvalues.appendChild(listedvalues);

});


function getJsonData() {
    const elements = document.getElementById('elements').value;
    const json_file = `/api/${elements}/`;

fetch(json_file)
.then(response => response.json())
.then(jsonData => {
    
const json_data_values = document.getElementById('json_data_values');
json_data_values.innerHTML = ' ';

jsonData.forEach(item => {

const divvalues = document.createElement('div');
const radiovalues = (item.options && item.options.length > 0)
? item.options.map((option, index) => `
    <input type="radio" id="option${index + 1}" name="options" value="${option}" />
    <label for="option${index + 1}">${option}</label>
  `).join('') 
: (item.qs && item.qs.length > 0)
  ? item.qs.map((q, index) => `
      <input type="radio" id="question${index + 1}" name="questions" value="${q}" />
      <label for="question${index + 1}">${q}</label>
    `).join('')
  : '<textarea name="text"></textarea>';


divvalues.innerHTML = `
<form>
<p>${item.title}</p>
<p>${item.desc || item.description}</p>
<div>
${radiovalues}

</div>

<hr>
</form>
`;
json_data_values.appendChild(divvalues);
});
})
.catch(error => console.error('Error fetching JSON:', error));

}

getJsonData();

console.log(getJsonData())