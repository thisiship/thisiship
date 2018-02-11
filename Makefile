fetch:
	date >> logs/fetch.log
	python fetch_event.py >> logs/fetch.log

clean:
	date >> logs/clean.log
	python event_cleanup.py >> logs/clean.log

create:
	date >> logs/create.log
	python create_index.py >> logs/create.log

discover:
	date >> logs/discover.log
	python discovery.py >> logs/discover.log

daily:
	make clean
	make discover
	make fetch
	make create

event_count:
	ls -l jsondump/ | wc -l

automatic:
	git pull
	make daily
	git add index.html event_list.txt
	git commit -m "daily run"
	git push
