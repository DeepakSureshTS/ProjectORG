async function validatetoken(){
    var status = false;
    await $.ajax({
     
            url:"http://"+window.location.hostname+":8000/token_authentication",
            type:"GET",
            headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token'),
      },
            success:function(data) {
       
              document.getElementById("email_token").innerHTML = data.Loggedemail.token;
              // console.log(data)
              // console.log(data.Loggedemail.token)
            },
            error: function(xhr, ajaxOptions, thrownError){                    
                status = false
                return status
            }
    })
    return status
  }  

function logout(){
    localStorage.removeItem('access_token')
    window.location.href = "../../../Frontend/index.html"
  }