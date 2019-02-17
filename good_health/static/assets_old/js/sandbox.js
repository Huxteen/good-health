
$(document).ready(function () {

    // To query the database for the search fields
    let $myForm = $('#ajax-medical-record-filter');
    $myForm.submit(function (event) {
        event.preventDefault();
        let $filterFormAPI = document.getElementById("medical-conditions")
        let $filterBy = $filterFormAPI.value;
        let $filterField = $filterFormAPI.getAttribute("data-field");
        let $queryURL = "/api/medical-record-filter?" + $filterField + "=" + $filterBy;

        // let ourRequest = new XMLHttpRequest();
        // ourRequest.open("GET", $queryURL);
        // ourRequest.onload = function () {
        //     console.log(ourRequest.responseText);
        //     var ourData = JSON.parse(ourRequest.responseText);
        //     console.log(ourData)
        // }
        // ourRequest.send();



        $.ajax({
            method: 'GET',
            url: $queryURL,
            success: handleSuccess,
            error: handleError,
            processData: false,
            contentType: false,
            cache: false,
        });
        function handleSuccess(data) {
            console.log(data);
        }
        function handleError(ThrowError) {
            console.log(ThrowError)
        }
    });




});







// Ajax call request

// let filterFormAPI = document.getElementById("ajax-search-api");
let filterFormAPI = document.getElementById("ajax-medical-record-filter");
let filterFormAPI2 = document.getElementById("btn");
let searchAPI = document.getElementById("ourcontainer");
let medicalCondition = document.getElementById("medical-conditions").value;
let thisURL = "/api/medical-record-filter?medical_condition=malaria";
// let thisURL = filterFormAPI.attr('action') || window.location.href;



// alert(medicalCondition)

// filterFormAPI2.addEventListener("click", function (event) {
//     event.preventDefault();
//     let medicalCondition1 = document.getElementById("medical-conditions").value;
//     alert(medicalCondition1);
// });

// filterFormAPI2.addEventListener("onload", function (event) {
//     event.preventDefault();
//     alert(medicalCondition);
// });




// $.ajax({
//     method: 'GET',
//     url: thisURL,
//     success: function(data){
//         console.log(data)
//         console.log("success")
//     },
//     error: function(error_data){
//         console.log(error_data)
//     }
// })



// filterFormAPI.addEventListener("submit", function(event){
//     event.preventDefault();
//     let ourRequest = new XMLHttpRequest();
//     ourRequest.open("GET", thisURL);
//     ourRequest.onload = function(){
//         console.log(ourRequest.responseText);
//         var ourData = JSON.parse(ourRequest.responseText);
//         console.log(ourData)
//     }
//     ourRequest.send();


// });

