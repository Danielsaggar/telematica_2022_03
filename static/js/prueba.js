x=0;
i=0
function act(){        
    fetch('/data')
    .then(res => res.json())
    .then(data => {                    
            if(x<data[0]){                
                x=data[0]     
                const app = document.querySelector(".envivo");           
                const label = document.createElement("label");
                label.innerHTML = "<label>Comentarista: "+data[1] +"<br></label>"; // <div>Hola a todos</div>                
                app.insertAdjacentElement("afterbegin", label);       
            }                                 
        });            
    if(i==5){
    const comentar = document.querySelector("#Activate");
    comentar.textContent ="Activo"; // <div>Hola a todos</div>
    comentar.textContent;
    }   
    i++;     
}
act()
setInterval(act, 500)