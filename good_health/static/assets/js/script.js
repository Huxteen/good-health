$(document).on('submit', '#new_user_form', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/all_medical_report/',
        data:{
            search_element: $('#search_element').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function () {

        }
    });
});