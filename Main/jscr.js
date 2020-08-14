 function validateform(){  
  var fname=document.forms["sform"]["Fname"].value;  
  var email=document.forms["sform"]["Email"].value;
  var password=document.forms["sform"]["Password"].value;
  var repassword=document.forms["sform"]["RePassword"].value;
  var contact=document.forms["sform"]["Contact"].value;
  var city=document.forms["sform"]["City"].value;
  var address=document.forms["sform"]["Address"].value;
  
  var chkpassword=/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;
   var phoneno = /^\d{10}$/;

  if (fname=="" || fname== null){  
      alert("Name can't be blank");  
    return false;  
  }
  if(email==""){
  	alert("Enter email id");
  	return false;
  }
  if(password==""){  
      alert("Password required");  
    return false;  
    }  
   if(!password.match(chkpassword)){  
      alert("Password should be atleast 7 characters with atlest one numeric and a special character");  
    return false;  
    }  
    if(repassword==""){  
      alert("Password required");  
    return false;  
    }  
    if(repassword!=password){
    	alert("Password doesn't match");
    	return false;
    }
    if(!contact.match(phoneno)){
    	alert("Enter a valid phone number containing 10 digits");
    	return false;
    }
    if(city==""){  
      alert("Information required for Newspaper subscription");  
    return false; 
	}
    if(address==""){  
      alert("Information required for Newspaper subscription");  
    return false; 
	}
    return true;
     
}  