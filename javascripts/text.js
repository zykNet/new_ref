function move_on(element,far,to,cishu,time) {
    var add=(to%2==1)?true:false;
    var num=(to<3)?((element.style.marginLeft==="")?0:parseInt(element.style.marginLeft)):((element.style.marginTop==="")?0:parseInt(element.style.marginTop));
    var max=(to%2==1)?(num+far):num;
    var min=(to%2==1)?num:(num+far);
    var time=setInterval(function  () {
        if(add){
            num++;
            (to<3)?(element.style.marginLeft=num+"px"):(element.style.marginTop=num+"px");
            if(num>=max){
                add=false;
                cishu--;
                if(cishu==0){clearInterval(time)}
            }
        }else{
            num--;
            (to<3)?(element.style.marginLeft=num+"px"):(element.style.marginTop=num+"px");
            if(num<=min){
                add=true;
                cishu--;
                if(cishu==0){clearInterval(time)}
            }
        }
    },time);
}
