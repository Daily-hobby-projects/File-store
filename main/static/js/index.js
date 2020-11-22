const file_input=document.querySelector('#file-input');
const imageNameDisplay=document.querySelector('.image-name');

file_input.addEventListener('input',()=>{
    imageNameDisplay.innerText=file_input.value;
})