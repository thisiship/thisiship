function occur_on_same_day(filter_date, event_date) {
	return filter_date.toDateString() === event_date.toDateString();
}
function show_all_events() {
	$(".event").show();
}
$(document).ready(function() {
	var now_datetime = new Date();

	$("#filter-submit").click(function() {
		//$("#filter-by-date").val()
		$(".filter-master").each(function () {
			alert($(this).val());
		});
		var event_tags = $(".event");
		filter_option = {};
		$("#city-filter option:selected").each(function() {
			city = $(this).val();
			if (city != 0 ) {
				filter_option.city = city;
			}
		});

		$("#state-filter option:selected").each(function() {
			state = $(this).val();
			if (state != 0) {
				filter_option.state = state;
			}
		});

		$("#venue-filter option:selected").each(function() {
			venue = $(this).val();
			if (venue != 0) {
				filter_option.venue = venue;
			}
		});
		// if there is anything to filter on
		if (Object.keys(filter_option).length > 0) {
			event_tags.hide();
			event_tags.each(function() {
				city_match = true;
				state_match = true;
				venue_match = true;
				date_match = true;
				var $this = $(this);
				if ("city" in filter_option) {
					city_match = $this.find(".city").text().trim() === filter_option.city; 
				}

				if ("state" in filter_option) {
					state_match = $this.find(".state").text().trim() === filter_option.state;
				}

				if ("venue" in filter_option) {
					venue_match = $this.find(".venue").text().trim() === filter_option.venue;
				}

				if("date" in filter_option) {
					date_match = occur_on_same_day(filter_option.date, $this.find(".start_datetime").val())
				}

				if (city_match && state_match && venue_match && date_match) {
					$(this).show();
				}
			});
		} else {
			// this means all the filters are on "All X"
			show_all_events();
		}
		//send info to GA
		gtag('event','filter', {
			'event_label': 'submit'
		});
		console.log('Submit Button Event Sent');
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
