$(function(){
	//selecteur de search dans le DOM de lobject'''
	$('#search')
	//to avoid autocomplete => autocomplete ="off" in the template
	.keyup(function(){

		//to avoid a heavy search from the first letter
		if ( $('#search').val().length > 1) 
		{		
			$.ajax({
				type:"POST",
				url: "/ajx1/search/", //path to the url in url.py
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
	$('#search-results').html(data);
}