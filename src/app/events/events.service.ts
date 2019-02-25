import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

import { MusicEvent } from './music-event.model';

@Injectable({
  providedIn: 'root'
})
export class EventsService {
  musicEventSub = new Subject<MusicEvent[]>();

  events: MusicEvent[] = [
    {
      title: 'Event 1',
      description: 'Wicked cool event',
      startDate: '2019-02-25 14:02:03.894240',
      endDate: '2019-02-25 14:02:03.894240',
      price: 10
    },
    {
      title: 'Event 2',
      description: 'Another great event',
      startDate: '2019-02-25 14:02:03.894240',
      endDate: '2019-02-25 14:02:03.894240',
      price: 15
    },
    {
      title: 'Event 3',
      description: 'less good event..',
      startDate: '2019-02-25 14:02:03.894240',
      endDate: '2019-02-25 14:02:03.894240',
      price: 5
    }
  ];

  constructor() { }

  getMusicEventSubscription() {
    return this.musicEventSub.asObservable();
  }

  getAllEvents() {
    return this.events.slice();
  }
  addEvent(musicEvent: MusicEvent) {
    this.events.push(musicEvent);
    this.musicEventSub.next(this.events.slice());
  }
}
