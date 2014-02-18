$(document).ready(function(){ //equivalent $(function(){})

    // Can specify a custom tick Array.
    // Ticks should match up one for each y value (category) in the series.
    var ticks = cities;
     
    var plot1 = $.jqplot('chartdiv_1', series, {
        // The "seriesDefaults" option is an options object that will
        // be applied to all series in the chart.
        seriesDefaults:{
            renderer:$.jqplot.BarRenderer,
            rendererOptions: {fillToZero: true},
             pointLabels: { show: true, location: 'n', edgeTolerance: -10 } //"n" for north 
        },
        // Custom labels for the series are specified with the "label"
        // option on the series option.  Here a series option object
        // is specified for each series.
        series:[
            {label:'Nombre total'},
            {label:'Nombre médicalisé'},
            {label:'Dépenses'}
        ],
        // Show the legend and put it outside the grid, but inside the
        // plot container, shrinking the grid to accomodate the legend.
        // A value of "outside" would not shrink the grid and allow
        // the legend to overflow the container.
        legend: {
            show: true,
            placement: 'outsideGrid'
        },
        axes: {
            // Use a category axis on the x axis and use our custom ticks.
            xaxis: {
                renderer: $.jqplot.CategoryAxisRenderer,
                ticks: ticks
            },
            // Pad the y axis just a little so bars can get close to, but
            // not touch, the grid boundaries.  1.2 is the default padding.
            yaxis: {
                pad: 1.05,
                tickOptions: {formatString: '%d'}
            }
        }
    });
});

