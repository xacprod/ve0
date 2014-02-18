README.AJAX.TIP!!

At the time you attach the hover event handler, you do not have any elements with the "city_found" class. There are two ways to fix this:

(1) You can delay setting the event handler until after the elements are added:

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results').html(data).find(".city_found").hover(function(){
        alert( "click" );
    });
}
(2) You could use event delegation:

$(document).on("hover", ".city_found", function() {
    alert( "click" );
});
"""
Shouldn't it be from the "search-results" div that I should set the delegation? –  sana 22 hours ago   
 	
@sana - With event delegation you are attaching a "hover" handler on the document, 
but it will only call the function when the target element has the "city_found" class. 
You would put that code right where you originally had $(".city_fond").hover(function(){ alert( "click" ); });. 
But you don't need to do both (1) & (2), just one of them. –  John S 21 hours ago 