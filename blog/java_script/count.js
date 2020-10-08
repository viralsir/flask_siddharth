if(!localStorage.getItem('cnt'))
{
    localStorage.setItem('cnt',0);
}
    //let cnt=0
        function count()
        {
               cnt=localStorage.getItem('cnt');
               cnt++;
               document.querySelector("h1").innerHTML=cnt;
               localStorage.setItem('cnt',cnt);
              /* if (cnt % 5 === 0)
               {
                   alert(`counter is reached to ${cnt}`)
               }*/
        }
        document.addEventListener('DOMContentLoaded',function(){
            document.querySelector("button").onclick=count;
            document.querySelector("h1").innerHTML=localStorage.getItem('cnt');
           // setInterval(count,1000);
        })

