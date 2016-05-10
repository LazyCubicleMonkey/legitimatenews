'use strict'

$( document ).ready(function() {
	$('.inner').hide(0);
	var speed = 500;
	var handler = function(ev) {
		var target = $(ev.target);
		var elId = target.attr('id');
		var articles = document.getElementsByClassName("articles");
		var curElement = document.getElementById(elId);
		if(!curElement)
			return;
		for (var i = 0; i < articles.length; i++) { 
			var article = articles[i];
			if(curElement.contains(article))
				return $('#' + elId + ' .inner').stop(true, true);
		}
	};
	
	var enterHandler = function (ev) {
		var comp = handler.call(null, ev);
		if(comp) {
				
			//if(outerWidth > width) {
				var articles = $(comp).find(".articles");
					var width = $(comp).width();
					var outerWidth = $(comp).outerWidth();
					var innerWidth = $(comp).innerWidth();
					/*console.log("Articles width: " + $(articles).width());
					console.log("Articles inner width: " + $(articles).innerWidth());
					console.log("Articles outer width: " + $(articles).outerWidth());
					console.log("Articles scroll width: " + $(articles)[0].scrollWidth);*/
				//while(outerWidth > width) {
					console.log("Width: " + width);
					console.log("Outer width: " + outerWidth);
					//console.log("Scroll width: " +  $(comp)[0].scrollWidth);
					console.log("Inner width: " + innerWidth);
					var curSize = window.getComputedStyle(articles[0], null).getPropertyValue('font-size');
					var fontSize = parseInt(curSize.substring(0, curSize.length - 2));
					console.log("Current font size: " + curSize + " font size: " + fontSize);
					fontSize = 12;
					for(var i = 0;i < articles.length; i++) {
						var article = articles[i];
						console.log("Article width: " +  $(article).width());
						/*var width = $(article).width();
						var outerWidth = $(article).outerWidth();
						var innerWidth = $(article).innerWidth();
						console.log("xWidth: " + width);
						console.log("xOuter width: " + outerWidth);
						console.log("xScroll width: " +  $(article)[0].scrollWidth);
						console.log("xInner width: " + innerWidth);*/
						article.style.fontSize = fontSize + "px";
					}
					var w = $(comp).width();
					outerWidth = $(comp).outerWidth();
					innerWidth = $(comp).innerWidth();
				//}
				//console.log(articles);
				//comp[0].style.fontSize = comp[0].style.fontSize - 5;
			//}
			comp.slideToggle(speed);
		}

	};
	
	var exitHandler = function (ev) {
		var comp = handler.call(null, ev);
		if(comp)
			comp.slideUp(speed);
	};
	
	$('.outer').mouseenter(enterHandler).mouseleave( exitHandler);
});