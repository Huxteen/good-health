$(document).ready(function(){

    // To Initialise the Date picker
     $("#datepicker-view-start").datepicker({
        autoClose: true,
        viewStart: 2
    });


    // To add an Organization to database
    let $myForm = $('#my-ajax-form');
    $myForm.submit(function(event){
        event.preventDefault();
        // var $formData = $myForm.serialize();
        let $formData = new FormData($($myForm)[0]);
        // var $formData = new FormData(this);      
        let $thisURL = $myForm.attr('action') || window.location.href;
        
        $.ajax({
            method: 'POST',
            url: $thisURL,
            data: $formData,
            success: handleSuccess,
            error: handleError,
            processData: false,
            contentType: false,
            cache: false,
        });
        function handleSuccess(data){
            console.log(data);
            $("#js-response-status div").remove()
            if (data.status == 'success')  {
                let founded = moment(data.founded).format("MMM DD, YYYY");
                let $actionIcons = "<td><a href='#' class='btn btn-info btn-xs'><i class='fa fa-pencil'></i></a>&nbsp;&nbsp;<a href='#' class='btn btn-danger btn-xs'><i class='fa fa-trash'></i></a></td>";
                let $tableData = "<tr><td>" + data.name + "</td><td> " + data.type + "</td><td>" + founded + "</td>" + $actionIcons; 
                if($("#js-update-org tr").length >= 10){
                    $("#js-update-org tr:last-child").remove()
                }                
                $("#js-update-org").prepend($tableData);
                let $template = '<div class="alert col-md-12 alert-success alert-dismissible" role = "alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Congratulations! &nbsp;</strong>' + data.message + '</div>';
                $("#js-response-status").prepend($template);
                $myForm[0].reset()
            }else{
                let $template = '<div class="alert col-md-12 alert-danger alert-dismissible" role = "alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Oops! &nbsp;</strong>' + data.message + '</div>';
                $("#js-response-status").prepend($template);
                
            }
        }
        function handleError(ThrowError){
            console.log(ThrowError)
        }
    });
});