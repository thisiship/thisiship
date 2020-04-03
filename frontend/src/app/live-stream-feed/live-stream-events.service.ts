import { Injectable } from '@angular/core';
import { LiveStreamEvent } from './live-stream-event.model';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LiveStreamEventsService {
  liveStreamEvents: LiveStreamEvent[] = [
    // enter real prod data here for now
    {
      title: 'Rochester LiveStream Music Festival',
      artistName: 'Varied. See event for details.',
      startDatetime: new Date('2020-04-03T12:00:00'),
      endDatetime: new Date('2020-04-05T23:30:00'),
      facebookLink: 'https://www.facebook.com/events/1102403476795976/',
      youtubeLink: 'https://www.youtube.com/watch?v=41F-Qe6_NAA',
    }
  ];

  liveStreamEventsSub: BehaviorSubject<LiveStreamEvent[]>;

  constructor() {
    // this.liveStreamEvents = this.createLiveStreamsMock();
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
        facebookLink: 'https://www.facebook.com',
        youtubeLink: 'https://www.youtube.com',
    });
    for (let i = 0; i < 5; i++) {
      lsList.push({
        title: 'Test Event Title',
        artistName: 'TestUser',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com',
        youtubeLink: 'https://www.youtube.com',

      });
    }
    lsList.push({
        title: 'Really Long Live Stream Event Title',
        artistName: 'Test Artist With a Longer Name',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com',
        youtubeLink: 'https://www.youtube.com',

    });
    lsList.push({
        title: 'Really Long Live Stream Event Title',
        artistName: 'Test Artist With a Longer Name',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com',
        youtubeLink: 'https://www.youtube.com',

    });
    for (let i = 0; i < 5; i++) {
      lsList.push({
        title: 'Test Event Title',
        artistName: 'TestUser',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com',
        youtubeLink: 'https://www.youtube.com',

      });
    }
    lsList.push({
        title: 'Really Long Live Stream Event Title',
        artistName: 'Test Artist With a Longer Name',
        startDatetime: new Date(),
        endDatetime: new Date(),
        facebookLink: 'https://www.facebook.com',
        youtubeLink: 'https://www.youtube.com',

    });
    return lsList;
  }
}
