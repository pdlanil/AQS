$(document).ready(function () {
    $('#all').click(function () { 
        $('#business-tab').show();
        $('#health-tab').show();
        $('#house-tab').show();
        $('#vehicle-tab').show();
    });


    $('#business').click(function () { 
       $('#business-tab').show();
       $('#health-tab').hide();
       $('#house-tab').hide();
       $('#vehicle-tab').hide();
        
    });

    $('#health').click(function () { 
        $('#health-tab').show();
        $('#business-tab').hide();
        $('#house-tab').hide();
        $('#vehicle-tab').hide();
         
     });

     $('#house').click(function () { 
        $('#house-tab').show();
        $('#health-tab').hide();
        $('#business-tab').hide();
        $('#vehicle-tab').hide();
         
     });

     $('#vehicle').click(function () { 
        $('#vehicle-tab').show();
        $('#health-tab').hide();
        $('#house-tab').hide();
        $('#business-tab').hide();
         
     });

});