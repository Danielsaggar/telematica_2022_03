function act(){        
    fetch('/score')
    .then(res => res.json())
    .then(data => {                    
            const AmarillaL = document.querySelector("#AmarillaL");
            AmarillaL.textContent = data[0]; 
            AmarillaL.textContent;
            const AmarillaV = document.querySelector("#AmarillaV");
            AmarillaV.textContent = data[1]; 
            AmarillaV.textContent;
            const RojaL = document.querySelector("#RojaL");
            RojaL.textContent = data[2]; 
            RojaL.textContent;
            const RojaV = document.querySelector("#RojaV");
            RojaV.textContent = data[3]; 
            RojaV.textContent;
            const GolesL = document.querySelector("#GolesL");
            GolesL.textContent = data[4]; 
            GolesL.textContent;
            const GolesV = document.querySelector("#GolesV");
            GolesV.textContent = data[5]; 
            GolesV.textContent;
            const EsquinaL = document.querySelector("#EsquinaL");
            EsquinaL.textContent = data[6]; 
            EsquinaL.textContent;
            const EsquinaV = document.querySelector("#EsquinaV");
            EsquinaV.textContent = data[7]; 
            EsquinaV.textContent;
            const ArcoL = document.querySelector("#ArcoL");
            ArcoL.textContent = data[8]; 
            ArcoL.textContent;
            const ArcoV = document.querySelector("#ArcoV");
            ArcoV.textContent = data[9]; 
            ArcoV.textContent;
            const OffsiteL = document.querySelector("#OffsiteL");
            OffsiteL.textContent = data[10]; 
            OffsiteL.textContent;
            const OffsiteV = document.querySelector("#OffsiteV");
            OffsiteV.textContent = data[11]; 
            OffsiteV.textContent;            
        });          
}
act()
setInterval(act, 500)