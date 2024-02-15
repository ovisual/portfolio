let mt=document.getElementById('meter')
let km=document.getElementById('kilometer')
let inc=document.getElementById('inches')
let yd=document.getElementById('yard')
let rf=document.getElementById('refresh')

mt.oninput= calculatetherest
function calculatetherest(){
    let usermt=mt.value
    km.value=usermt/1000
    inc.value=usermt*37.91
    yd.value=usermt*1.0936

}
km.oninput= calculatetherest2

function calculatetherest2(){
    let usermt=km.value
    mt.value=usermt*1000
    inc.value=usermt*39370
    yd.value=usermt*1093.61
}

rf.onclick= clearall2
function clearall(){
    location.reload()
}

function clearall2(){
    mt.value=''
    km.value=''
    inc.value=''
    yd.value=''
}
