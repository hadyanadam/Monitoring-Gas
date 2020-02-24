const months = ["Jan", "Feb", "Mar","Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
setInterval(function(){
    nilai.forEach(function(item,index){
        document.getElementById("myTbody").rows[index].cells[2].innerHTML = "<center>"+ item +"</center>";
    });
    timestamp.forEach(function(item,index){
        let waktu = new Date(item);
        let new_minute;
        let minute = waktu.getMinutes();
        if(minute < 10){new_minute = "0" + minute;}
        let converted_date = months[waktu.getMonth()] + ". " + waktu.getDate() + ", " + waktu.getFullYear() + ", " + waktu.getHours() + ":" + new_minute;
        document.getElementById("myTbody").rows[index].cells[1].innerHTML = "<center>"+converted_date+"</center>";
    });
},5000);