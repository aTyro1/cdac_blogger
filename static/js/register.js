function ValidateEmail() 
{
    if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.getElementById('email').value))
    {
        return (true)
    }
    else
    {
            alert("You have entered an invalid email address!")
            document.getElementById('email').focus()
            document.getElementById('email').value=''
            
            return (false)
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
function deleteAccount()
{
    val=`<div class="container mx-auto">
    <form method="POST" action="delete">
        <input type="password" class="p-4 w-screen" placeholder="ENTER YOUR PASSWORD! " name="password" style="text-align: center; ">
        <input type="submit" value='delete' class="mt-2 p-2 shadow-lg rounded" style="background-color: #1b3ba3; color: #F4F27E;">
    </form>
</div>
    `
    document.getElementById('content').innerHTML=val;
    
}
function changePassword()
{
    val=`<div class="container mx-auto">
    <form method="POST" action="changePassword">
        <input type="password" class="p-4 w-screen" placeholder="ENTER CURRENT PASSWORD " name="current_password" style="text-align: center; ">
        <input type="password" class="p-4 w-screen" placeholder="ENTER NEW PASSWORD " name="new_password1" style="text-align: center; ">
        <input type="password" class="p-4 w-screen" placeholder="RE-ENTER NEW PASSWORD " name="new_password2" style="text-align: center; ">
        <input type="submit" value='change' class="mt-2 p-2 shadow-lg rounded" style="background-color: #1b3ba3; color: #F4F27E;">
    </form>
</div>`
    document.getElementById('content').innerHTML=val;
}
function logout()
{
    val=`<div class="container mx-auto">
    <form method="get" action="logout">
        <input type="submit" value='submit' class="mt-2 p-2 shadow-lg rounded" style="background-color: #1b3ba3; color: #F4F27E;">
    </form>
</div>
    `
    document.getElementById('content').innerHTML=val;
}
function startmic()
{
    alert("starting....");
}
