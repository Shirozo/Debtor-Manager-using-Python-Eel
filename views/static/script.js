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
    data_confirmation.style = "revert"
    data.value = "";
    data.style = "revert";
    var show = document.getElementById("change_pass");
    if (show.style.top === "-25%" || !(show.style.top)){
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
        if (NewPassword.value.trim() != confirmation.value.trim() || await eel.login(confirmation.value.trim())()){
            $("#new_password").css({"border" : "red solid 1px", "outline":"red solid 1px"})
            $("#confirmation").css({"border" : "red solid 1px", "outline":"red solid 1px"})
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
    var confirmed = document.getElementById("confirmation").value;
    await eel.change_pass(confirmed);
    $("#pass_data").css("display", "none");
    $("#success").css("display", "block"); 
    $("#change_pass").css("top", "-25%");
}   

function loan(){
    var table = document.querySelector("table");
    if (!(table.style.filter) || table.style.filter === "blur(0px)"){
        $("#add_loan").css("display", "revert");
        table.style.filter = "blur(6px)";
        table.setAttribute("style", "-webkit-filter: blur(6px)");
        table.disabled = true;
    }
}

function close_win(){
    var table = document.querySelector("table");
    table.style.filter = "blur(0)";
    table.setAttribute("style", "-webkit-filter: blur(0)");
    $("#add_loan").css("display", "none");
}

function ensure_no_space(){
    var val = document.getElementById("loan_name");
    if (val.value.trim() === ""){
        $("#loan_name").css({"outline":"red solid 1px", "border":"solid red 1px"});
    }
    else{
        val.style = "revert";
    }
}

function ensure_number(){
    var loan_amount = document
}