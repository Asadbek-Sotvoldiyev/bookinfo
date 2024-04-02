$(function() {
	$('.sidebar .widget ul li:first-child').addClass('first');
	$('#navigation ul li:first-child').addClass('first');
	$('#navigation ul li:last-child').addClass('last');
	$('.footer-nav ul li:first-child').addClass('first');

	$('a.popup').colorbox({
		onComplete: function(){
			$.colorbox.resize();
		}
	});
	 $(document).on('click', '#logout', function(e){
        $.ajax({
            type:"POST",
            url:"{% url 'users:logout' %}",
            data:{
                message:'salom',
                action:'post',
                csrfmiddlewaretoken:"{% csrf_token %}",
            },
            success:function(json){
                location.reload()
            }
        })
    })
});
