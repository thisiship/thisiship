fetch:
	python fetch_event.py

clean:
	python event_cleanup.py

create:
	python create_index.py

daily:
	make clean
	make fetch
	make create
