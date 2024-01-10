function ValidateEmail() 
{
    if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.getElementById('email').value))
    {
        return (true)
    }
    else
    {
            document.getElementById('email').value=''
            document.getElementById('email').focus()
            alert("You have entered an invalid email address!")
    }
    return (false)
}
function matchPassword()
{
    if(document.getElementById('password1').value!=document.getElementById('password2').value)
    {
        // document.getElementById('password2').value='';
        // document.getElementById('password2').focus();
        alert('Your Password did not match. PLEASE ENTER AGAIN!')
    }
    return (false)
}
function pushComment()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log('hello')
    }
    };
    query_string="new_comment="+document.getElementById('new_comment').value+"&id="+document.getElementById('blog_id').value;
     xhttp.open("GET", "/home/reload?"+query_string, true);
     xhttp.send();
}