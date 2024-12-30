const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navLogo = document.querySelector('#navbar__logo')

//Mobile Menu
menu.addEventListener('click', function(){
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
});


function Home() {
    window.location.href = "3Dhtml.html";
}
function Pictures() {
    window.location.href = "3DPictures.html";
}
function Links() {
    window.location.href = "3DLinks.html";
}
function Specials() {
    window.location.href = "NewYears.html";
}
function About() {
    window.location.href = "3DAbout.html";
}
function Order() {
    window.location.href = "3DOrder.html";
}


