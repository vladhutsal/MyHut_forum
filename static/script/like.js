$(document).ready(function() {

    $('.vote_up_button').on('click', function() {
        
        var member_id = $(this).attr('value');
        
        request = $.ajax({
            url : '/update',
            type : 'POST',
            data : {  }
        })

    });

});