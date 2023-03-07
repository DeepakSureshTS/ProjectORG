function signUpData(){
    let userName = document.querySelector("#typeUserName").value
    let emailData = document.querySelector("#typeEmail").value
    let passWord = document.querySelector("#typePassword").value

  
      $.ajax({
     
       url:"http://"+window.location.hostname+":8000/signup",
       dataType: "json",
            contentType: "application/json",
      type:"POST",
      data:JSON.stringify({
        username:userName,
        email:emailData,
        password:passWord

      }),
      success:function(data) {
        console.log(data)
        
         window.location.href = "http://"+window.location.hostname+":5500/../../Frontend/templates/Login.html";
        
      },
      error: function(xhr){
        console.log(xhr.responseJSON.detail)
      
        alert (xhr.responseJSON.detail)
      }
    })            
    
  }