function O2O_UTIL(){
	this.index = 9999;
	this.time = {};
	this.timefun = {};//定时回调
	this.timemess = {};
	this.parms = {};
	setInterval(this.timer,1000);//定时扫描窗口是否关闭
}
O2O_UTIL.prototype={
	createMask : function(num){
		this.index = this.index+1;
		//$('.mask_box').remove();
		var height = $(document).height(); 
		$(document.body).append('<div class="mask_box mask_'+num+'" style="height:'+height+'px;z-index:'+this.index+'"></div>');
	},
	//全选择或反选
	checkboxAll : function(obj,num){
		if(typeof(num)=='undefined')num=0;
		obj = $(obj);
		var table = obj.parents('table');
		if(table.length>0){
			var tbody = table.find('tbody,thead,tfoot');
			var tmp = tbody.find('tr').find('td:eq('+num+') input[type=checkbox]');
			for(var i=0;i<tmp.length;i++){
				var k = $(tmp[i]);
				if(obj.is(':checked')!=k.is(':checked')){
					k.click();
				}
			}
		}
	},
	//获取选择的值
	checkboxAllValue : function(obj,num){
		if(typeof(num)=='undefined')num=0;
		obj = $(obj);
		var table = obj.parents('table');
		var str = "";
		if(table.length>0){
			var tbody = table.find('tbody');
			var arrs = tbody.find('tr').find('td:eq('+num+') input[type=checkbox]:checked');
			for(var i=0;i<arrs.length;i++){
				if(str!="")str+=",";
				str+=$(arrs[i]).val();
			}
		}
		return str;
	},
	timer : function(){
		for(var k in util.time){
			if(util.time[k]!=""){
				util.time[k] = util.time[k]-1;
				if(util.time[k]<1){
					util.time[k]="";
					util.closeAlert(k,util.timefun[''+k]);
				}else{
					var key = util.timemess[''+k];
					if(typeof(key)=='undefined')
						$('.alert_'+k+" .sure").text('（'+(util.time[k])+' s）');
					else
						$('.alert_'+k+' .alert_time').html(key.replace('{0}',(util.time[k]+1)));
				}
			}
		}
	},
	alert : function(mess,time,model,surefun){
		var num = parseInt(Math.random()*10000000000);
		if(typeof(model)=='undefined')model=false;
		if(model)this.createMask(num);
		var top = parseInt(($(window).height()-130)/2);
		var left = parseInt(($(window).width()-300)/2);
		this.index = this.index+1;
		var tpl = "<div class='alert_box alert_"+num+"' style='top:"+top+"px;left:"+left+"px;z-index:"+this.index+"'><div class='alert_close' onclick='util.closeAlert("+num+")'></div><div class='alert_content'></div><div class='alert_button'></div></div>";
		$(document.body).append(tpl);
		$('.alert_'+num+' .alert_content').text(mess);
		var text= "确 定";
		if(time>0){
			this.time[''+num]=time;
			this.timefun[''+num]=window[surefun];
			text = "（"+time+" s）"
		}
		$('.alert_'+num+' .alert_button').append('<button class="sure" onclick="util.closeAlert('+num+')">'+text+'</button>');
		return 'alert_'+num;
	},
	window : function(config,surefun){
		var cf ={title:'',bsure:true,tsure:'确 定',tcancel:'取 消',bcancel:false,timemess:'',time:0,icon:'',width:200,height:30,url:'',ele:'',model:true,mess:'',nav:'',align:'left'};
		for(var k in cf){if(typeof(config[k])=='undefined')config[k]=cf[k];}
		var num = parseInt(Math.random()*10000000000);
		if(typeof(model)=='undefined')model=true;
		if(model)this.createMask(num);
		var th = 60;
		if(config.bsure||config.bcancel)th=100;
		var top = parseInt(($(window).height()-(config.height+th))/2);
		var left = parseInt(($(window).width()-(config.width+20))/2);
		this.index = this.index+1;
		var tpl = "<div class='alert_box alert_"+num+"' style='top:"+top+"px;z-index:"+this.index+";left:"+left+"px;width:"+(config.width+20)+"px;height:"+(config.height+th)+"px;'><div class='alert_title'>"+config.title+"</div><div class='alert_close' onclick='util.closeAlert("+num+")'></div><div class='alert_content' style='width:"+(config.width)+"px;height:"+(config.height)+"px;'></div><div class='alert_button'></div></div>";
		$(document.body).append(tpl);
		// 渲染本页元素
		if(config.mess!=''){
			var size = 14;
			if(config.nav!="")size=16;
			var text = "<table><tr><td class='alert_icon'></td><td><div class='alert_text' style='text-align:"+config.align+";font-size:"+size+"px'>"+config.mess+"</div><div class='alert_nav' style='text-align:"+config.align+"'>"+config.nav+"</div><div class='alert_time' style='text-align:"+config.align+"'></div></td></tr></table>";
			$('.alert_'+num+' .alert_content').html(text);
//			if(config.icon!='')$('.alert_'+num+' .alert_icon').append('<div class="'+config.icon+'"></div>');
			if(config.icon!='')$('.alert_'+num+' .alert_icon').addClass(config.icon);
		}else if(config.ele!='')$('.alert_'+num+' .alert_content').html($('#'+config.ele).html());
		else if(config.url!='')$('.alert_'+num+' .alert_content').html("<iframe style='width:"+(config.width)+"px;height:"+(config.height)+"px;' frameborder='0' src='"+config.url+"'></iframe>");
		// 渲染按钮
		this.parms[''+num] = arguments;//组装参数
		var text = config.tsure;
		// 渲染时间
		if(config.time>0){
			this.timemess[''+num]=config.timemess;	
			this.timefun[''+num]=window[surefun];
			this.time[''+num]=config.time;
			text = "（"+config.time+" s）"
		}
		if(config.bsure)$('.alert_'+num+' .alert_button').append('<button class="sure" onclick="util.closeAlert('+num+','+surefun+')">'+text+'</button>');
		if(config.bcancel)$('.alert_'+num+' .alert_button').append('<button class="cancel" onclick="util.closeAlert('+num+')">'+config.tcancel+'</button>');
		util.placeholder();
		return 'alert_'+num;
	},
	confirm : function(mess,surefun){
		var num = parseInt(Math.random()*10000000000);
		this.createMask(num);
		var top = parseInt(($(window).height()-130)/2);
		var left = parseInt(($(window).width()-300)/2);
		this.index = this.index+1;
		var tpl = "<div class='alert_box alert_"+num+"' style='top:"+top+"px;left:"+left+"px;z-index:"+this.index+"'><div class='alert_close' onclick='util.closeAlert("+num+")'></div><div class='alert_content'></div><div class='alert_button'></div></div>";
		$(document.body).append(tpl);
		$('.alert_'+num+' .alert_content').text(mess);
		this.parms[''+num] = arguments;//组装参数
		$('.alert_'+num+' .alert_button').append('<button class="sure" onclick="util.closeAlert('+num+','+surefun+')">确 定</button>');
		$('.alert_'+num+' .alert_button').append('<button class="cancel" onclick="util.closeAlert('+num+')">取 消</button>');
		return 'alert_'+num;
	},
	closeAlert : function(num,fun){
		if(fun){
			var arrs = [],p = this.parms[''+num];
			arrs[0]="alert_"+num;
			if(p)for(var i=2;i<p.length;i++){arrs[arrs.length]=p[i];}
			fun.call(this,arrs);
		}else{
			this.time[''+num]=0;
			$('.mask_'+num).remove();
			$('.alert_'+num).remove();
		}
	},
	closeWindow : function(num){
		num = num.replace('alert_','');
		this.time[''+num]=0;
		$('.mask_'+num).remove();
		$('.alert_'+num).remove();
	},
	// 去掉未选中的CHECKBOX/radio
	removeCR : function(id){
		var arrs = $('#'+id+" .form-radio");
		for(var i=0;i<arrs.length;i++){
			var obj = $(arrs[i]);
			if(obj.find('input').is(':checked')){//选中
				obj.find('input').remove();
			}else
				obj.remove();
		}
	},
	//错误提示
	tipError : function(obj,mess,pos,type){
		var tagName = obj.tagName;
		obj = $(obj);
		var num = parseInt(Math.random()*10000000000);
		//清除原来样式
		if(obj.attr('tipe')){
			$('.'+obj.attr('tipe')).remove();
			obj.removeClass('o2o-object');
		}
		var html = "<div class='o2o-error "+type+" to_"+num+"'>&nbsp;"+mess+"</div>";
		if(tagName=="div"||tagName=="DIV"){//兼容COMBOX
			var temp = obj.find('input');
			obj.addClass('o2o-object');
			temp.unbind('focus').focus(function(){
				$(this).parent().removeClass('o2o-object');
				$('.to_'+num).remove();
			});
		}else{
			obj.addClass('o2o-object').unbind('focus').focus(function(){
				obj.removeClass('o2o-object');
				$('.to_'+num).remove();
			});
		}
		$(obj).attr('tipe',"to_"+num).after(html);
		if(typeof(pos)=='undefined')pos={top:0,left:0};
		$('.to_'+num).css({top:(obj.offset().top+obj.outerHeight()-1-pos.top)+"px",left:(obj.offset().left-pos.left)+"px"}).width(obj.outerWidth()-2).show();
	},
	placeholder : function(){//兼容IE8
		var arry = $('[placeholder]');
		for(var i=0;i<arry.length;i++){
			var obj = $(arry[i]);
			if(obj.val()==''||obj.attr('placeholder')==obj.val()){
				obj.css({'color':'#cccccc'}).val(obj.attr('placeholder'));
			}
		}
		arry.unbind('focus,blur').bind({
			focus : function(){
				var obj = $(this);
				if(obj.attr('placeholder')==obj.val()){
					obj.css({'color':'#363636'}).val('');
				}
			},
			blur : function(){
				var obj = $(this);
				if(obj.val()==''){
					obj.css({'color':'#cccccc'}).val(obj.attr('placeholder'));
				}else{
					obj.css({'color':'#363636'});
				}
			}
		});
	},
	debug : function(){
		$('a[href=#]').not('[onclick]').attr('href',"javascript:util.alert('功能完善中，敬请期待！',3);");
	}
}
var util = new O2O_UTIL();

$(document).ready(function(){
  util.debug();
  util.placeholder();
});