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
	});
	$("#filter-reset").click(function() {
		$(".filter-master").val('0');
		$("#filter-submit").trigger("click");
	});
	/*
	$(".desc-btn").click(function() {
		var event_id = $(this).siblings(".ev-id").first().text().trim();
		console.log("Sending info to GA: "  + event_id);
		ga('send','event', 'button', 'description', event_id);
		console.log("GA Finished");
	});
	/* try outbound link 
	$(".fb-link").click(function() {
		var event_id = $(this).siblings(".ev-id").first().text();
		console.log("Sending info to GA: " + event_id);
		gtag('send', 'event', 'button', 'facebook', event_id);
		console.log("GA Finished");
	});
	*/
});
