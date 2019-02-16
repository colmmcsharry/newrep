$( document ).ready(function() {
	$("#target").click(function() {
		$.get( "/hackernews", function( data ) {
			console.log(data);
			for (var i=0; i< data.length; i++) {
				var current_title = data[i];
				console.log(current_title);
				$( "#hackernews" ).append(`<div>${current_title}</div>`);
				// var newdiv = $('<div class ='box' />');

				// data.append(newdiv);
			}
		  
		});
	});
});

