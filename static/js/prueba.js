x=0;
i=0
function act(){        
    fetch('/data')
    .then(res => res.json())
    .then(data => {                    
            console.log("Esta es la data 1 =",data)
            console.log("X: "+x);
            if(x<data[0]){
                console.log("Data: "+data);
                console.log("Tamaño: "+data.length);
                console.log("Posición 0: "+data[0]);
                console.log("Posición 1: "+data[1]);
                x=data[0]                
                const label = document.createElement("label");
                label.innerHTML = "<label>Comentarista: "+data[1] +"<br></label>"; // <div>Hola a todos</div>
                document.body.appendChild(label); 
                
                        
            }                                 
        });      
    console.log("i: "+i);     
    if(i==5){
    const comentar = document.querySelector("#Activate");
    comentar.textContent ="Activo"; // <div>Hola a todos</div>
    comentar.textContent;
    }   
    i++;     
}
act()
setInterval(act, 1500)