fetch:
	python fetch_event.py

clean:
	python event_cleanup.py

create:
	python create_index.py

discover:
	python discovery.py

daily:
	make clean
	make discover
	make fetch
	make create

event_count:
	ls -l jsondump/ | wc -l
