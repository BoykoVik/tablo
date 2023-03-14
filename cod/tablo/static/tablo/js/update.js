jQuery(document).ready(function(){
    send_ajax()
    console.log('111')
    });

function send_ajax() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
    headers: {'X-CSRFToken': csrftoken},
    url: 'getupdate',
    type: 'GET',

    success: function(data) {
        update_data(data)
    }
});
}

function update_data(data){
    console.log(data);
    const parsedData = JSON.parse(data);
    console.log(parsedData)
}