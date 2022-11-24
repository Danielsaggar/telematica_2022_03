(function(){
    const sliders = [...document.querySelectorAll('.tablas__body')];
    const buttonNext = document.querySelector('#next');
    const buttonBefore = document.querySelector('#before');
    let value;

    buttonNext.addEventListener('click',()=>{
        changePosition(1);



    });

    buttonBefore.addEventListener('click',()=>{
        changePosition(-1);      



    });

    const changePosition = (add)=>{
        const currentTable = document.querySelector('.tablas__body--show').dataset.id;
        value = Number(currentTable);
        value+=add;

        sliders[Number(currentTable)-1].classList.remove('table__body--show');

        if(value == sliders.length+1 || value == 0){
            value = value === 0 ? sliders.length :1;
        }

        sliders[value-1].classList.add('table__body--show');

        console.log(value);
    }

    
})();