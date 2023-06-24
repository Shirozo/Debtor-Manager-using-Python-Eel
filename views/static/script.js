async function logg(){
    var password = document.getElementById("password").value;
    var status = await eel.login(password)();
    if (status == "True"){
        alert("True");
        location.href = "templates/index.html";
    }
    else{
        var to_show = document.getElementsById("invalid");
        alert("pass")
    }
}