// navbar visibility
const navbar = document.querySelector('.nav-fixed');
window.onscroll = () => {
    if (window.scrollY > 70) {
        navbar.classList.add('nav-active');
    } else {
        navbar.classList.remove('nav-active');
    }
};

// loader
const showLoad = document.querySelector('.loader');

window.addEventListener('load',()=>{
    setTimeout(() => {
        showLoad.classList.add('disappear');
    },2000)
})