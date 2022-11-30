function act(){        
    fetch('/teams')
    .then(res => res.json())
    .then(data => {           
        console.log(data.length) 
        const app = document.querySelector("#Grupo");     
        console.log(app.value)   
        var select = document.getElementById('Grupo');
        select.addEventListener('change',
        function(){
            for(i=0; i<data.length; i++){
                if(app.value==data[i][1]){
                    console.log(data[i][0])  
                    const label = document.createElement("option");
                    label.value = data[i][0];           
                    label.textContent = data[i][0];   
                    app.insertAdjacentElement("afterbegin", label);
                }              
            }
        });  
        
        });            
}
act()
setInterval(act, 500)