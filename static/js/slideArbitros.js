(function(){
    const titleAdmins = [...document.querySelectorAll('.Admin__title')];
    console.log(titleAdmins)

    titleAdmins.forEach(Admin =>{
        Admin.addEventListener('click',()=>{
            let height = 0;
            let answer = Admin.nextElementSibling;
            let addPadding = Admin.parentElement.parentElement;


            addPadding.classList.toggle('Admin__padding--add');
            Admin.children[0].classList.toggle('Admin__arrow--rotate');

            if(answer.clientHeight === 0){
                height = answer.scrollHeight;
            }

            answer.style.height = `${height}px`;
        });

    });

})();