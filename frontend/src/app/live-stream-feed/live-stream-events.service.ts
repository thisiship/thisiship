import { Injectable } from '@angular/core';
import { LiveStreamEvent } from './live-stream-event.model';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LiveStreamEventsService {
  liveStreamEvents: LiveStreamEvent[] = [
    // enter real prod data here for now
  ];

  liveStreamEventsSub: BehaviorSubject<LiveStreamEvent[]>;

  constructor() {
    this.liveStreamEvents = this.createLiveStreamsMock();
    this.liveStreamEventsSub = new BehaviorSubject<LiveStreamEvent[]>(this.liveStreamEvents);
  }

  getLiveStreamEventSubscription() {
    return this.liveStreamEventsSub.asObservable();
  }

  createLiveStreamsMock() {
    const lsList = [];
    lsList.push({
        title: 'Really Long Live Stream Event Title',
        artistName: 'Test Artist With a Longer Name',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com'
    });
    for (let i = 0; i < 5; i++) {
      lsList.push({
        title: 'Test Event Title',
        artistName: 'TestUser',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com'
      });
    }
    lsList.push({
        title: 'Really Long Live Stream Event Title',
        artistName: 'Test Artist With a Longer Name',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com'
    });
    lsList.push({
        title: 'Really Long Live Stream Event Title',
        artistName: 'Test Artist With a Longer Name',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com'
    });
    for (let i = 0; i < 5; i++) {
      lsList.push({
        title: 'Test Event Title',
        artistName: 'TestUser',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com'
      });
    }
    lsList.push({
        title: 'Really Long Live Stream Event Title',
        artistName: 'Test Artist With a Longer Name',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com'
    });
    return lsList;
  }
}
