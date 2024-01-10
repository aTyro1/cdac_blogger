function ValidateEmail() 
{
    val=document.getElementById('email').value;
    if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(val))
    {
        return (true)
    }
    else
        alert("You have entered an invalid email address!")
    return (false)
}