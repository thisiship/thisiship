import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';

import { LiveStreamEvent, } from './live-stream-event.model';
import { LiveStreamEventsService } from './live-stream-events.service';

@Component({
  selector: 'app-live-stream-feed',
  templateUrl: './live-stream-feed.component.html',
  styleUrls: ['./live-stream-feed.component.sass']
})
export class LiveStreamFeedComponent implements OnInit, OnDestroy {
  liveStreamEvents: LiveStreamEvent[] = [];

  liveStreamEventSubscription: Subscription;

  constructor(private liveStreamEventsService: LiveStreamEventsService) {
  }

  ngOnInit() {
    this.liveStreamEventSubscription = this.liveStreamEventsService.getLiveStreamEventSubscription()
    .subscribe((liveStreamEvents: LiveStreamEvent[]) => {
      this.liveStreamEvents = liveStreamEvents;
    });
  }

  ngOnDestroy() {
    this.liveStreamEventSubscription.unsubscribe();
  }

  getDateDisplayValue(date: Date) {
    return `${date.toDateString()} at ${date.getHours()}:${date.getMinutes()}`;
  }
}
