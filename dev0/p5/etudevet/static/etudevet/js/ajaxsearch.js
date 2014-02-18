$(function(){
	//selecteur de search dans le DOM de lobject'''
	
	$("#search").keyup(function(){
		if ( $('#search').val().length > 0) //to avoid a heavy search from the first letter
		{
			$.ajax({
				type:"POST",
				url: "/etudevet/search/", //path to the url in url.py
				data:{
					'search_text' : $('#search').val(),
					'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
				},
				success: searchSuccess,
				dataType: "html"
			});
			}
	});
});


function searchSuccess(data, textStatus, jqXHR)
{
	$('#search-results').html(data).find(".city_found").click(function(){
		console.log($(".city_found").attr('id'));
		$.ajax({
			type:"POST",
			url: "/etudevet/display/", //path to the url in url.py
			data:{
				'city_to_display' : $(".city_found").attr('id'),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: displaySuccess,
			dataType: "html"
		});
	});	
}


function displaySuccess(data, textStatus, jqXHR)
{
	$('#city-display').html(data);
}