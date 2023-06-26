async function logg(){
    var error_code = document.getElementById("error_code");
    var password = document.getElementById("password").value;
    var status = await eel.login(password)();
    if (status){
        window.location.href = "../templates/index.html";
    }
    else{
        error_code.style.display = "inline-block";
    }
}


function show_change_pass(){
    var image = document.getElementById("success");
    image.style.display = "none";
    var pass_data = document.getElementById("pass_data");
    pass_data.style.display = "block";
    var data = document.getElementById("new_password");
    var data_confirmation = document.getElementById("confirmation");
    data_confirmation.value = "";
    data.value = "";
    var show = document.getElementById("change_pass");
    if (show.style.top === "-25%"){
        show.style.display = "block";
        show.style.top = "10%";
    }
    else{
        show.style.top = "-25%";
    }
    validate();
}

async function validate(){
    var NewPassword = document.getElementById("new_password");
    var confirmation = document.getElementById("confirmation");
    var changeBtn = document.getElementById("changeP");
    changeBtn.disabled = true;
    if (NewPassword.value.trim() === "" || confirmation.value.trim() === ""){
        changeBtn.disabled = true;
    }
    else{
        if (NewPassword.value.trim() != confirmation.value.trim()){
            NewPassword.style.border = "red solid 1px";
            NewPassword.style.outline = "red solid 1px";
            confirmation.style.border = "red solid 1px";
            confirmation.style.outline = "red solid 1px";
            changeBtn.disabled = true;
        }
        else{
            NewPassword.style.border = "green solid 1px";
            NewPassword.style.outline = "green solid 1px";
            confirmation.style.border = "green solid 1px";
            confirmation.style.outline = "green solid 1px";
            changeBtn.disabled = false;
        }
    }
}

async function passChange(){
    var animate = document.getElementById("change_pass");
    var to_hide = document.getElementById("pass_data");
    var success = document.getElementById("success");
    var confirmed = document.getElementById("confirmation").value;
    await eel.change_pass(confirmed);
    to_hide.style.display = "none";
    success.style.display = "block";
    animate.style.top = "-25%";
}   