$( function () {
	String.prototype.linkify = function() {
	return this.replace(/[A-Za-z]+:\/\/[A-Za-z0-9-_]+\.[A-Za-z0-9-_:%&\?\/.=]+/, function(m) {
        return m.link(m);
	}); }; 


	var $ali, $current, $lis, $holder;

	$holder = $('.article-select')
	$ali = $('.article-select li');
	$current =  $('.current');
	$lis = $('.article-select li:not(.current)');
	
	$('.article-select').css({'overflow':'hidden'});
	$lis.hide();
	$('.article-select').hover ( function () {
		$current.addClass('inactive');
		$(this).css({'height':'auto'});
		$lis.show();
	}, function () {
		$current.removeClass('inactive');
		$lis.hide();
		$(this).css({'height':'40px'});
	});
	
	var url = "http://twitter.com/status/user_timeline/davidnuon.json?count=1&callback=?";
	$.getJSON(url, function(data){
		var test = data[0].text.linkify().replace(/@(\w+)/g, '<a href="http://twitter.com/$1">@$1</a>')
		.replace(/#(\w+)/g, '#<a href="http://twitter.com/search?q=%23$1">$1</a>');
		$('#footer_twitter').html(test);
	});
	
	$('#copy').html('&copy;')
	$('#p_ai span').each( function () {
		$(this).html('&nbsp;&nbsp;&nbsp;&nbsp;' + $(this).html());
	});
});
