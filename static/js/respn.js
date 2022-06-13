burger = document.querySelector('.burger')
navbar = document.querySelector('.navbar')
rightnav = document.querySelector('.rightnav')
navlist = document.querySelector('.nav-list')

burger.addEventListener('click', ()=>{
    rightnav.classList.toggle('v-class');
    navlist.addEventListener.toggle('v-class');
    navbar.addEventListener.toggle('h-nav');
})