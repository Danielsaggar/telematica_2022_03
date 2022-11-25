function table(){
    $.ajax({
        url: "../Telematica/php/query1.php", //change to your php file (in my example data.php)
        type: "GET",
        dataType: "JSON",
        data: {}, //this is data you send to your server
        success: function(res) {
          console.log(res);
          console.log(res.length);
      
          for (i = 0; i < res.length; i++) {
            $('#testing').append(
                '<tr><td>' + res[i]['Pos'] +
                '</td><td>' + res[i]['Equipo'] + 
                '</td><td>' + res[i]['PJ'] + 
                '</td><td>' + res[i]['G'] +
                '</td><td>' + res[i]['E'] +
                '</td><td>' + res[i]['P'] +
                '</td><td>' + res[i]['GF'] +
                '</td><td>' + res[i]['GC'] +
                '</td><td>' + res[i]['DG'] +
                '</td><td>' + res[i]['Pts'] +
                '</td></tr>')
          }
      
        }
      })
}
table();