$('chat').click(function () {
        $.ajax({
            url: '/api/calc?a=' + document.getElementById('message').value ,
            success: function(data){
                $('#self').html(data['res']);
            }
           
        });
    });
