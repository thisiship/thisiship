$(document).ready(function() {
	// filter on city
	$(".city-filter").change(function() {
		var event_tags = $(".event");
		var option = "";
		$(".city-filter option:selected").each(function() {
			option = $(this).text().trim();
		});
		console.log(option);
		if (option === "All Cities") {
			event_tags.show();
		} else {
			event_tags.hide();
			var matching = ".city:contains(" + option + ")";
			$(matching).closest('.event').show();
		}
	});
});
