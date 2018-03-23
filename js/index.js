function show_all_events() {
	$(".event").show();
}

$(document).ready(function() {
	var now_datetime = new Date();

	$(".filter-master").change(function () {
		show_all_events();
		filter_id = $(this).attr('id');
		filter_val = $(this).val();
		var filter_options = {};
		$(".filter-master").filter(function () {
			var option_value = $(this).val();
			return option_value != '0' && option_value != "";
		}).each(function() {
			//data-target will have a class name as its value
			var targ = "." + $(this).data('target');
			// filter_by_class : value of filter
			filter_options[targ] = $(this).val();
		});
		$(".event").each(function () {
			var current_event = $(this);
			Object.entries(filter_options).forEach(([key,value]) => {
				//get the value of closes filter_by_class (key)
				current_value = current_event.find(key).attr('value').toLowerCase();
				if (current_value !== value) {
					current_event.hide();
				}
			});
		});
		//send info to GA
		gtag('event', filter_id, {
			'event_label': filter_val
		});
		console.log('Filter Event Sent: ' + filter_id + " " + filter_val);
	});

	$("#filter-reset").click(function() {
		$(".filter-master").val('0');
		show_all_events();
		//send info to GA
		gtag('event','filter', {
			'event_label': 'reset'
		});
		console.log('Reset Button Event Sent');
	});

	$(".desc-btn").click(function() {
		var event_id = $(this).siblings(".fb-link").first().attr("href");
		//send info to GA
		gtag('event', 'description', {
			'event_label': event_id
		});
		console.log('Description Button For Event ' + event_id + ' Sent');
	});
	$(".fb-link").click(function() {
		var event_link = $(this).attr("href");
		//send info to GA
		gtag('event', 'facebook_link', {
			'event_label': event_link
		});
		console.log("Facebook: " + event_link + ' Sent.');
	});
	$(".promo-link").click(function() {
		var dest = $(this).attr("href");
		gtag('event', 'promo_link', {
			'event_label': dest
		});
		console.log('Promotion clicked for ' + dest + ' Sent');
	});
});
