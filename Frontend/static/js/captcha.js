var captcha;
function generate() {

   
        var alpha = new Array('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z');
        var i;
        for (i=0;i<4;i++){
          var a = alpha[Math.floor(Math.random() * alpha.length)];
          var b = alpha[Math.floor(Math.random() * alpha.length)];
          var c = alpha[Math.floor(Math.random() * alpha.length)];
          var d = alpha[Math.floor(Math.random() * alpha.length)];
          var e = alpha[Math.floor(Math.random() * alpha.length)];
          var f = alpha[Math.floor(Math.random() * alpha.length)];
         }
       var code = a + '' + b + '' + '' + c + '' + d+''+e +''+f;
       document.getElementById("mainCaptcha").value = code
     }

     function CheckValidCaptcha(){
        var string1 = removeSpaces(document.getElementById('mainCaptcha').value);
        var string2 = removeSpaces(document.getElementById('txtInput').value);
        if (string1 == string2){
          document.getElementById("error").style.display = "none";
    // document.getElementById('success').innerHTML = "Form is validated Successfully";
          // alert("Form is validated Successfully");
          authorise()
          return true;
        }
        else{
          document.getElementById("error").style.display = "block";       
    document.getElementById('error').innerHTML = "Invalid Captcha";
        //  alert("Please enter a valid captcha.");
          return false;
        }
    }
    function removeSpaces(string){
      return string.split(' ').join('');
    }



function authorise(){
let emailData = document.querySelector("#mail").value
let passWord = document.querySelector("#password").value

  $.ajax({
  
    url:"http://"+window.location.hostname+":8000/login",
    type:"POST",
    dataType: "json",
            contentType: "application/json",
    data:JSON.stringify({
      email:emailData,
      password:passWord

    }),
   success:function(data) {
     console.log(data.access_token)
    
      localStorage.setItem("access_token", data.access_token)  
      // window.location.href = "http://"+window.location.hostname+":5500/../../Frontend/templates/dashboard.html";
      window.location.href = "../../templates/dashboard.html";
   
     
    },
    error: function(xhr, ajaxOptions, thrownError){
      console.log(xhr.responseJSON.detail)
      document.getElementById("error").style.display = "block";       
      document.getElementById('error').innerHTML =xhr.responseJSON.detail;
      //  alert (xhr.responseJSON.detail)

    }
    
   
 })


 
}




  
