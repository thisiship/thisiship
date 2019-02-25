import { Component, OnInit } from '@angular/core';
import { EventsService } from '../events.service';
import { MusicEvent } from '../music-event.model';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-event-list',
  templateUrl: './event-list.component.html',
  styleUrls: ['./event-list.component.css']
})
export class EventListComponent implements OnInit {
  events: MusicEvent[] = [];
  eventsSub: Subscription;

  constructor(private eventsService: EventsService) { }

  ngOnInit() {
    this.events = this.eventsService.getAllEvents();
    this.eventsSub = this.eventsService.getMusicEventSubscription()
    .subscribe((events: MusicEvent[]) => {
      this.events = events;
    });
  }

}
