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
            var articles = $(comp).find(".articles");
            var width = $(comp).width();
            var outerWidth = $(comp).outerWidth();
            var innerWidth = $(comp).innerWidth();
            var curSize = window.getComputedStyle(articles[0], null).getPropertyValue('font-size');
            var fontSize = parseInt(curSize.substring(0, curSize.length - 2));
            fontSize = 12;
            for(var i = 0;i < articles.length; i++) {
                var article = articles[i];
                article.style.fontSize = fontSize + "px";
            }
            var w = $(comp).width();
            outerWidth = $(comp).outerWidth();
            innerWidth = $(comp).innerWidth();
            comp.slideToggle(speed);
		}
	};
	
	var exitHandler = function (ev) {
		var comp = handler.call(null, ev);
		if(comp)
			comp.slideUp(speed);
	};
	
	$('.outer').mouseenter(enterHandler).mouseleave(exitHandler);

	$("#search_form").submit( function(eventObj) {
	    var inputs = $('#search_form :input');
	    var oldVal = inputs[0].value;
	    inputs[0].value = "site:legitimatenews.com " + inputs[0].value;
	    //Keeps the above part hidden from user
	    setTimeout(function() {
            inputs[0].value = oldVal;
        }, 0);
        return true;
    });

    var hover = function() {
        if (!document.body.currentStyle) return;
        var DIVcomments = document.getElementById('comments');
        var DIVcomment_wrap = document.getElementById('comment-wrap');
        DIVcomments.onmouseover = function() {
            DIVcomment_wrap.style.display = 'block';
        }
        DIVcomments.onmouseout = function() {
            DIVcomment_wrap.style.display = 'none';
        }
    }
    window.onload = hover;
});