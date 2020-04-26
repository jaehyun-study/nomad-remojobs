const form = document.querySelector('form');
const button = document.querySelector('button');

if (form && button) {
    form.addEventListener('submit', ()=>{
        button.disabled=true
    });
}
