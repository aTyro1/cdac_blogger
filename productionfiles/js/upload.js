function uploadimg()
{
    let input = document.createElement('input');
    input.type = 'file';
    input.accept='image/*'
    input.style='visibility:hidden;';
    input.name='uploaded';
    input.onchange = _ => {
            let files =   Array.from(input.files);
            let child=` <div class="container" style="display: inline; margin-left: 10px;">
            <input type="text" readonly value='`+files[0].name+`' style="padding: 2px; font-size: 10px; color: #1b3ba3;">
        </div>`;
            node= document.getElementById('images').innerHTML+=child;
        };
    input.click();
    document.getElementById('uplf').appendChild(input);
}