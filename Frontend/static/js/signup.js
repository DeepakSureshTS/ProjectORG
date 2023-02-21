function signUpData(){
    let userName = document.querySelector("#typeUserName").value
    let emailData = document.querySelector("#typeEmail").value
    let passWord = document.querySelector("#typePassword").value

    var re = new RegExp("(?=^.{8,}$)((?=.*\d)|(?=.*))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$");
    if (re.test(passWord)) {
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
        window.location.href = "http://"+window.location.hostname+":5500/../../templates/Login.html";
        return(data)
      },
      error: function(xhr, ajaxOptions, thrownError){
        alert ("User with this name already exist")
      }
    })            
    } else {
      alert("Invalid Pattern for password")
    }
  }