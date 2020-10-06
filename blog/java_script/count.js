 let cnt=0
        function count()
        {
               cnt++;
               document.querySelector("h1").innerHTML=cnt;

              /* if (cnt % 5 === 0)
               {
                   alert(`counter is reached to ${cnt}`)
               }*/
        }
        document.addEventListener('DOMContentLoaded',function(){
            document.querySelector("button").onclick=count;

            setInterval(count,1000);
        })

