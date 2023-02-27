async function validatetoken(){
    var status = false;
    await $.ajax({
     
            url:"http://"+window.location.hostname+":8000/token_authentication",
            type:"GET",
            headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token'),
      },
            success:function(data) {
              status = data
            },
            error: function(xhr, ajaxOptions, thrownError){                    
                status = false
                return status
            }
    })
    return status
  }
  