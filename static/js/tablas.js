function table(){
    const xhttp = new XMLHttpRequest(); //creando el objeto para trabajar
    xhttp.onload = function(){
        var data = this.responseText
        data = JSON.parse(data);

        document.getElementById("Pos").innerHTML = data.Pos
        document.getElementById("Equipo").innerHTML = data.Equipo
        document.getElementById("PJ").innerHTML = data.PJ
        document.getElementById("G").innerHTML = data.G
        document.getElementById("E").innerHTML = data.E
        document.getElementById("P").innerHTML = data.P
        document.getElementById("GF").innerHTML = data.GF
        document.getElementById("GC").innerHTML = data.GC
        document.getElementById("DG").innerHTML = data.DG
        document.getElementById("Pts").innerHTML = data.Pts
        console.log(data)
    }

    xhttp.open("GET", "../Telematica/php/query.php"); // documento que estamos llamando
    xhttp.send();
    
}

setInterval(function(){ //creamos un intervalo para realizar el mismo request del archivo que genera la conexión con la base de datos
    table();
}, 500); // Cada 5 segundos