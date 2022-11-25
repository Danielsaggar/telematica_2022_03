function table(){
    $.ajax({
        url: "../Telematica/php/Estadios.php", //change to your php file (in my example data.php)
        type: "GET",
        dataType: "JSON",
        data: {}, //this is data you send to your server
        success: function(res) {
          console.log(res);
          console.log(res.length);
      
          for (i = 0; i < res.length; i++) {
            $('#Estadios').append(
                '<tr><td>' + res[i]['Estadio'] +
                '</td><td>' + res[i]['Capacidad'] +
                '</td><td>' + res[i]['Ubicación'] +
                '</td></tr>')
          }
      
        }
      })
}
table();