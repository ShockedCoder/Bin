function leConfirm(string) {
    var confirmation = confirm(string);
    if (confirmation) {
        window.location.replace("http://" + window.location.host.toString() + "/delete/0");
    } /* else {
        window.location.replace("http://" + window.location.host.toString());
    } */
}
