$(document).ready(function() {
	$("#filter-submit").click(function() {
		var event_tags = $(".event");
		filter_option = {};
		$("#city-filter option:selected").each(function() {
			city = $(this).text().trim();
			if (city !== "All Cities") {
				filter_option.city = city;
			}
		});

		$("#state-filter option:selected").each(function() {
			state = $(this).text().trim();
			if (state !== "All States") {
				filter_option.state = state;
			}
		});

		$("#venue-filter option:selected").each(function() {
			venue = $(this).text().trim();
			if (venue !== "All Venues") {
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

				if (city_match && state_match && venue_match) {
					$(this).show();
				}
			});
		} else {
			// this means all the filters are on "All X"
			event_tags.show();
		}
		//send info to GA
		gtag('event','filter', {
			'event_label': 'submit',
			hitCallback: function() {
				console.log('Submit Button Event Sent');
			}
		});

	});
	$("#filter-reset").click(function() {
		$(".filter-master").val('0');
		$("#filter-submit").trigger("click");
		//send info to GA
		gtag('event','filter', {
			'event_label': 'reset',
			hitCallback: function() {
				console.log('Reset Button Event Sent');
			}
		});
	});
	$(".desc-btn").click(function() {
		var event_id = $(this).siblings(".ev-id").first().text().trim();
		//send info to GA
		gtag('event', 'description', {
			'event_label': event_id,
			hitCallback: function() {
				console.log('Description for ' + event_id + ' sent to analytics.');
			}
		});
	});
	$(".fb-link").click(function() {
		var event_id = $(this).siblings(".ev-id").first().text();
		//send info to GA
		gtag('event', 'facebook_link', {
			'event_label': event_id,
			hitCallback: function() {
				console.log('Facebook Link for ' + event_id + ' sent to analytics.');
			}
		});
	});
});
