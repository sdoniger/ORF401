function getCookie(c_name) {

    var i,x,y,ARRcookies=document.cookie.split(";");
    for (i=0;i<ARRcookies.length;i++){
        x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
        y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
        x=x.replace(/^\s+|\s+$/g,"");
        if (x==c_name) {
            return unescape(y);
        }
    }
}

function setCookie(c_name,value,exdays) {

    var exdate=new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value=escape(value) + ((exdays==null) ? "" : ";expires="+exdate.toUTCString());
    document.cookie=c_name + "=" + c_value;
}

function checkCookie() {
    if (getCookie('first_visit') == 1){
        window.location.href = "/rides";
        } else {
            setCookie('first_visit',1,90);
        }
}


function checkForm() {
    var originationCity = document.getElementById('id_origination_city').value.trim();
    var destinationCity = document.getElementById('id_destination_city').value.trim();
    var originationState = document.getElementById('id_origination_state').value.trim();
    var destinationState = document.getElementById('id_destination_state').value.trim();

    // Check if all fields are empty
    if (!originationCity && !destinationCity && !originationState && !destinationState) {
        alert("Please fill in at least one field.");
        return false;
    }

    // Check if the user searches for "Elon Musk"
    if (originationCity.toLowerCase() === "elon musk" || destinationCity.toLowerCase() === "elon musk" || originationState.toLowerCase() === "elon musk" || destinationState.toLowerCase() === "elon musk") {
        alert("He's not here.");
        return false;
    }

    return true;
}


