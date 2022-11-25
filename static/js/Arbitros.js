function table(){
    $.ajax({
        url: "../Telematica/php/Arbitros.php", //change to your php file (in my example data.php)
        type: "GET",
        dataType: "JSON",
        data: {}, //this is data you send to your server
        success: function(res) {
          console.log(res);
          console.log(res.length);
      
          for (i = 0; i < res.length; i++) {
            $('#Arbitros').append(
                '<tr><td>' + res[i]['id_arbitro'] +
                '</td><td>' + res[i]['Nombre'] +
                '</td><td>' + res[i]['Procedencia'] +
                '</td></tr>')
          }
      
        }
      })
}
table();