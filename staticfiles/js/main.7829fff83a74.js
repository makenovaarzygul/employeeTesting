// ==============Check UserName Script=============
function checkUser(username) {
    var error = document.getElementById("error");
    var btn = document.getElementById("register-btn");
    var war = document.getElementById("warning");
    var req = new XMLHttpRequest();

    req.onload = function () {
        if (this.responseText == "true") {
            error.innerHTML = "Username Available";
            error.classList.add("alert-success");
            error.classList.remove("alert-danger");
            btn.disabled = false;
        } else {
            error.innerHTML = "Username Already Exist";
            error.classList.add("alert-danger");
            error.classList.remove("alert-success");
            btn.disabled = true;
        }
    };
    var l = username.length;
    if (l >= 4) {
        war.innerHTML = "";
        req.open(
            "GET",
            "/check-name?username=" + username,
            true
        );
        req.send();
    } else {
        error.classList.remove("alert-success");
        error.classList.remove("alert-danger");
        error.innerHTML = "";
        war.innerHTML = "";
        btn.disabled = true;
    }
    if (l <= 3) {
        btn.disabled = true;
        war.innerHTML = "*Minimum length 4 characters";
    }
}

// show password toggle

state=false
function showpass(){
    var passinput=document.getElementById('pass')
    var eye=document.getElementById('eye')
    if(state){
        passinput.setAttribute("type","password");
        state=false
        eye.classList.add('bx-show')
        eye.classList.remove('bxs-hide')
    }else{
        passinput.setAttribute('type','text')
        state=true
        eye.classList.add('bxs-hide')
        eye.classList.remove('bx-show')
        
    }
}