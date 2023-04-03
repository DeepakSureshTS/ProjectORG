async function validatetoken(){
    var status = false;
    await $.ajax({
     
            url:"http://"+window.location.hostname+":8000/token_authentication",
            type:"GET",
            headers: {"Authorization": 'Bearer ' + localStorage.getItem('access_token'),
      },
            success:function(data) {
              // console.log(data)
              // console.log(data.TokenDetails.token)
              document.getElementById("user_token").innerHTML = data.TokenDetails.LoggedUsername;
              
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
    window.location.href = "../../templates/Login.html"
    // window.location.href = "http://"+window.location.hostname+":5500/../../Frontend/templates/Login.html";
  }