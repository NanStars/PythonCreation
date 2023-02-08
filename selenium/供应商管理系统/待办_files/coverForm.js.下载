$(function(){
//	点击form页面下的a标签在头部导航显示内容
	$('#tableSort td a:not(.selflink) ').on('click',function(){
		window.parent.addTab($(this));
	});
	//	opentab类下的a标签在头部导航显示内容
	$('.opentab a:not(.selflink) ').on('click',function(){
		window.parent.addTab($(this));
	});
//	点击按钮显示对应弹框样式
	$('.defaultWin').click(function(){
		$('.defaultCover').css('display','block');
	})
	$('.withoutWin').click(function(){
		$('.withoutCover').css('display','block');
	})
	$('.containWin').click(function(){
		$('.containGin').css('display','block');
	})
//	点击定时关闭按钮显示遮罩,定时关闭遮罩
	$('.timeoffWin').click(function(){
		$('.timeoffCover').css('display','block');
		tim();
	})
	var wait=3;
	function tim(){
		if(wait==0){
			$('.timeoffCover').css('display','none');
			wait=3;
		}else{
			$('.timing').html(wait+'&nbsp;秒后关闭');
			wait--;
			setTimeout(function(){tim()},1000);
			}
	}
//	点击"小差号"关闭遮罩
	$('.closeCover').click(function(){
		$('.defaultCover,.withoutCover,.containGin').css('display','none');
	})
//	点击确定按钮关闭遮罩
	$('.sure').click(function(){
		$('.defaultCover,.withoutCover,.containGin').css('display','none');
	})	
//	点击取消按钮关闭遮罩
	$('.cancel').click(function(){
		$('.containGin').css('display','none');
	})	
//	点击任意不属于自己的地方,遮罩都消失
	$('.coverCont').click(function(){
		return false;		
	});
	
	$('.defaultCover,.withoutCover,.timeoffCover,.containGin').click(function(){
		$(this).css('display','none');	
	});

//表单页面
//		页面跳转按钮start
//	点击显示上一页/下一页
		var front=parseInt($('.front').html()); 
		var after=parseInt($('.after').html());
//				下一页
		$(".arrowRight").on("click",function () {
			if (front >= after) 
			{
				console.log(after)
				front = after;
				console.log("当前已经是最后一页！");
			}
			else if(front < after)
			{
				front ++;						
			//	$('.front').html(front);
				$('.jumpPage .pageNum').val(front);
				$('.jumpPage .pageButton').trigger("click");
			}						
		});
		//上一页
		$(".arrowLeft").on("click",function () {
			if (front <2) 
			{
				front = 1;
				console.log("当前已经是第一页！");
			}
			else
			{
				front --;						
			//	$('.front').html(front);
				$('.jumpPage .pageNum').val(front);
				$('.jumpPage .pageButton').trigger("click");
			}					
		});
								
//		$(".jumpPage .pageButton").on("click",function () {
////					
//			front = parseInt($(".jumpPage .pageNum").val());					
//			console.log(front);
//			if (front < 2 && front > after) 
//			{
//				front = 1;
//				$('.front').html(front);
//				console.log("返回首页！");
//			}
//			else
//			{			
//				$('.front').html(front);
//			}				
//		});	
		//页面跳转按钮end							
		//支持toggle兼容高版本jq
		$.fn.toggle = function( fn, fn2 ) {
		    var args = arguments,guid = fn.guid || $.guid++,i=0,
		    toggle = function( event ) {
		      var lastToggle = ( $._data( this, "lastToggle" + fn.guid ) || 0 ) % i;
		      $._data( this, "lastToggle" + fn.guid, lastToggle + 1 );
		      event.preventDefault();
		      return args[ lastToggle ].apply( this, arguments ) || false;
		    };
		    toggle.guid = guid;
		    while ( i < args.length ) {
		      args[ i++ ].guid = guid;
		    }
		    return this.click( toggle );
	  };
	
	//	文字筛选框start
			
			
		$('.n .searchBut').toggle(function(){
			$(this).siblings('div').css('display','block');
			$(this).css('border-radius',0);
		},function(){
			$(this).siblings('div').css('display','none');
			$(this).css('border-radius','4px');
		});

			
			$('.searchBox').on('click',function(){
				return false;
			})
			
			$('body').on('click',function(){
				$('.searchBox').css('display','none')
				$('.searchBut').css('border-radius','4px')
			})
	//	文字筛选框end
	
		$('.searchList li').on('click',function(){
			var searCont= $(this).html();
			if(searCont=="请再输入两个字符"||searCont=="没有找到匹配项"){
				return;
			}else{
				$('.searchBox').css('display','none');
				$('.searchBut').html(searCont);
				$('.searchBut').css('border-radius','4px');
				$('.searchIcon').val('');
				$('.searchList li:not(.prompt)').remove();
			}
		})
		
//	详情页面
	$('.deTitle li').on('click',function(){
		var index=$(this).index();
		$(this).addClass('cur').siblings().removeClass('cur');
		$(this).parent().siblings('div').eq(index).addClass('deShow').siblings('div').removeClass('deShow');
	})
	
//	折叠按钮
	$('.deFold').toggle(function(){
		$(this).parent().siblings('.deTable').css('display','none');
		$(this).addClass('deDown');
		
	},function(){
		$(this).parent().siblings('.deTable').css('display','');
		$(this).removeClass('deDown');
	})
	 

	})

//表格排序
function sortTable(table,idx){
    var otable=document.getElementById(table),
        otody=otable.tBodies[0],
        otr=otody.rows,
        tarr=[];
     for (var i = 1; i <otr.length; i++) {
           tarr[i-1]=otr[i];
     };

     if(otody.sortCol==idx){
        tarr.reverse();
     }else{
        tarr.sort(function(tr1,tr2){
            var value1 = tr1.cells[idx].innerHTML; 
            var value2 = tr2.cells[idx].innerHTML; 
            if(!isNaN(value1)&&!isNaN(value2)){
               return value1-value2;
            }else{
              return value1.localeCompare(value2);
             }           
        })
     }
     var fragment = document.createDocumentFragment();
     for (var i = 0; i <tarr.length; i++) {
         fragment.appendChild(tarr[i]);
     };
     otody.appendChild(fragment);
     otody.sortCol=idx;
  }
//	表单的宽度
	window.onload=function widthTable(){
		var thWidth = $('.table .listTitle th').length;
		var widthStr=Math.floor((100/thWidth)*100)/100;
		if(widthStr==6.25){
			widthStr=6.15;
		}
		$('.table tr th,.table tr td').css('width', widthStr+'%');
		$(".fromNumWidth").css("width", "3.66%");
		$(".fromNumWidth2").css("width", "9.66%");
		//设置跟进 备注宽度
		$(".fromNumWidth3").css("width", "45%");

		$(".fromNumWidth6").css("width", "4%");
		$(".fromNumWidth7").css("width", "6.9%");
		$(".tableWidth").css("width", "8.66%");
		$(".tableName").css("width", "4.66%");
	}

				
  //拖动
  function Drag(table){
    var ochek=document.getElementById("chenkbox"),
        otable=document.getElementById(table),
        otody=otable.tBodies[0],
        oth=otody.getElementsByTagName("th"),
        otd=otody.getElementsByTagName("td"),
        box=document.getElementById("box"),
        arrn=[];
        for (var i = 0; i < oth.length; i++) {
          oth[i].onmousedown=function(e){
              var e=e||window.event,
                  target = e.target||e.srcElement,
                  thW = target.offsetWidth,
                  maxl=ochek.offsetWidth-thW,
                  rows=otable.rows,
                  ckL=ochek.offsetLeft,
                  disX=target.offsetLeft,
                  _this=this,
                  cdisX=e.clientX-ckL-disX;
                  for (var i = 0; i < rows.length; i++) {
                      var op=document.createElement("p");
                      op.innerHTML=rows[i].cells[this.cellIndex].innerHTML;  
                      box.appendChild(op);
                  };    
                  for (var i = 0; i < oth.length; i++) {
                         arrn.push(oth[i].offsetLeft);      
                  }; 
                  console.log(arrn);
                  box.style.display="block";
                  box.style.width=thW+"px";
                  box.style.left=disX+"px";
                  //未完成 还有事件没写。
                  document.onmousemove=function(e){
                      var e=e||window.event,
                      target = e.target||e.srcElement,
                      thW = target.offsetWidth;
                      box.style.top=0;
                      box.style.left=e.clientX-ckL-cdisX+"px";
                      if(box.offsetLeft>maxl){
                           box.style.left=maxl+"px";
                      }else if(box.offsetLeft<0){
                           box.style.left=0;
                      }        
                      document.onselectstart=function(){return false};     
                    window.getSelection ? window.getSelection().removeAllRanges() : doc.selection.empty();              
                  }
                  document.onmouseup=function(e){
                     var e=e||window.event,
                         opr=box.getElementsByTagName("p"),
                         oboxl=box.offsetLeft+cdisX;
                        for (var i = 0; i < arrn.length; i++) {
                           if(arrn[i]<oboxl){
                            var index=i;
                           }
                        };
                       for (var i = 0; i < rows.length; i++) {
                          rows[i].cells[_this.cellIndex].innerHTML="";
                          rows[i].cells[_this.cellIndex].innerHTML=rows[i].cells[index].innerHTML;
                          rows[i].cells[index].innerHTML="";
                          rows[i].cells[index].innerHTML=opr[i].innerHTML;
                       };
                       box.innerHTML="";
                       arrn.splice(0,arrn.length);
                       box.style.display="none";
                       document.onmousemove=null; 
                       document.onmouseup=null;
                       document.onselectstart=function(){return false};     
                  }

             }
        };
  }


//验证页面输入非法字符
function inputCheck(str) {
	var regEn = /[`~!@#$%^&*_+<>?:"{},.\/;'[\]\=\+\-]/im,
		regCn = /[·！#￥——：；“”‘、，|《。》？、【】[\]]/im;

	if(regEn.test(str) || regCn.test(str)) {
		alert("输入不能包含特殊字符.");
		return false;
	}
	return true;
}
//Drag("tableSort");
