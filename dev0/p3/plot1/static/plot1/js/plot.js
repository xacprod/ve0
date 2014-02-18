//Each function to go through all arrays/objects provided by the view (here only 2, graph_data1, graph_data2)
$.each(graphs, function (i,e){

	//Create a new div to welcome the graph
	$('#chartdiv').append("<div id = chart_" + i +"></div>")

	//Define a variable that will be use to give the name of the target in jqplot
	var chart_x = 'chart_' + i

	//Create each graph => chart_x is the div target, e is the array (e.g. graph_data1)
	$.jqplot(chart_x,  [e], [{title:'My Plot',
								 axes:{yaxis:{min:230, max:1000}}
								}
							]);
	console.log(e) // Check the data in the console (optional)
}); 

