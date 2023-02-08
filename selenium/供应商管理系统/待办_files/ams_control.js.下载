$(function(){
	var winWidth=$(window).width();
	var len=$('.tabControl li').length;

//左侧的收缩面板按钮	
	var spend=0;
	$('.indexSpend').click(function(){
		if(spend==0){
			$('.indexCover').css('width','26px');
			$(this).addClass('spreadImg');
			$('.indexRightCont').addClass('shrinkWid');
			spend=1;
		}else{
			$('.indexCover').css('width','284px');
			$(this).removeClass('spreadImg');
			$('.indexRightCont').removeClass('shrinkWid');
			spend=0;
		}		
	})
	
//头部右侧
//	点击左侧展开、收缩菜单
	$('.indexLeft ul li:has(ul)').addClass('parent_li').find('>p').attr('data-type', 'lever-2');
    $('.indexLeft ul li p').siblings('ul').css('display','none');
	
	$('.indexLeft ul li.parent_li > p').on('click',function(e){
		var child =$(this).parent('li.parent_li').find('> ul>li');
		if (child.is(":visible")){
			child.hide('fast');
			$(this).attr('data-type','lever-1').find('>b').removeClass('downArrow');
			$(this).css('color','#000');
		}else{
        	$(this).siblings('ul').css({'display':'block','margin-left':'24px'});
			child.show('fast');
			$(this).attr('data-type', 'lever-2').find('>b').addClass('downArrow');
			$(this).css('color','#7e56c1');
		}
        e.stopPropagation();
	})

	
//	tab标签
//点击关闭tab标签
	$('.tabControl li span').live('click', function() {
	        // 获取标签名称
	        var tabid = $(this).siblings('b').attr("id");
	        // 删除选项卡和相关内容
	        var contentname = tabid + "_content";
	        $("#" + contentname).remove();
	        $(this).parent().remove();
			
	        //如果没有当前选项卡，如果还存在标签页，则显示第一个选项卡
	        if ($(".tabControl li.indexCurrent").length == 0 && $(".tabControl li").length > 0) {
	            //找到第一个选项卡  
	            var previous = $(".tabControl li:first-child");
	            previous.addClass("indexCurrent");
	            // 获取链接名称并显示相关内容
	            var pretabid = $(previous).find("b").attr("id");
	            $("#" + pretabid + "_content").show();
	        }else{
	        	//否則顯示默認的待辦
	        	$("#B_DEFAULT_content").show();
	        } 
	    });
            
//	点击标签获取当前关联内容
	
    $('.tabControl li b').live('click', function() {
        //获取内容标签名称
        var contentname = $(this).attr("id") + "_content";
        // 隐藏所有其他选项卡标签及其下内容
        $(".indexRightCont iframe").hide();
        $(".tabControl li").removeClass("indexCurrent");

        // 显示当前标签下内容
        $("#" + contentname).show();
        $(this).parent().addClass("indexCurrent");
    });
    
//	点击左侧的菜单，把其文字内容复制给tab标签里面
	$('.leftSecond p').live('click',function(){
		if($(this).siblings('ul').length>0){
			return;
		}else{
			 	addTab($(this));    
		}
	})
	 
	 
	$('.indexTabBut').toggle(function(){
		$('.indexTabStore').css('display','block');
	},function(){
		$('.indexTabStore').css('display','none');		
	})
	 
})
function addTab(link) {
    // 如果标签已经存在于列表中
	var tabname = $(link).html();
    if ($("#" + $(link).attr("data-tab")).length!=0)              {               	
         	var c=  $("#" + $(link).attr("data-tab") + "_content")
           	$(c).show().siblings('iframe').hide();
           	$("#" + $(link).attr("data-tab")).parent().addClass("indexCurrent").siblings().removeClass("indexCurrent");	                 
            return;
       }
    
    if ( $(link).attr("data-content")!=undefined && $(link).attr("data-content")!="" )              {               	
    	tabname = $(link).attr("data-content");
   }
    // 隐藏其他标签       
    $(".tabControl li").removeClass("indexCurrent");
    $(".indexRightCont iframe").hide();
    //添加新选项卡和相关内容
    $(".tabControl").append("<li class='indexCurrent'><b id='"+$(link).attr("data-tab")+"'>"+tabname+"</b><span></span></li>");
    $(".indexRightCont").append("<iframe src="+$(link).attr("data-src")+" id='" + $(link).attr("data-tab") + "_content' ></iframe>");               
//          添加
    $('.indexRightCont').children('iframe').css({'width':'100%','height':'100%','border':'none','min-width':1200});
    // 将新添加的选项卡设置为当前
    $("#" + $(link).attr("rel") + "_content").show();
}
