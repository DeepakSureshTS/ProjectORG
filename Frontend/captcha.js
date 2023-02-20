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


function printmsg() {
	const usr_input = document
		.getElementById("submit").value;
	
	// Check whether the input is equal
	// to generated captcha or not
	if (usr_input == captcha.innerHTML) {
		var s = document.getElementById("key")
			.innerHTML = "Matched";
		generate();
	}
	else {
		var s = document.getElementById("key")
			.innerHTML = "not Matched";
		generate();
	}
}
