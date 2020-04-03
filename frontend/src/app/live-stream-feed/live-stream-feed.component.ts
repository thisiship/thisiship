import { Component, OnInit } from '@angular/core';

import { LiveStreamEvent } from './live-stream-event.model';

@Component({
  selector: 'app-live-stream-feed',
  templateUrl: './live-stream-feed.component.html',
  styleUrls: ['./live-stream-feed.component.sass']
})
export class LiveStreamFeedComponent implements OnInit {

  livestreams: LiveStreamEvent[] = [];

  constructor() {
    this.livestreams = this.createLiveStreamsMock();
  }

  ngOnInit() {
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

  getDateDisplayValue(date: Date) {
    return `${date.toDateString()} at ${date.getHours()}:${date.getMinutes()}`;
  }
}
