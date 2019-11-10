import { Component, OnInit } from '@angular/core';
import { EventModel } from './event.model';

@Component({
  selector: 'app-event-feed',
  templateUrl: './event-feed.component.html',
  styleUrls: ['./event-feed.component.sass']
})
export class EventFeedComponent implements OnInit {
  events: EventModel[] = [
    {
      title: 'Forest Dwellers + others',
      venue: 'Tabernacle',
      startDate: new Date().toISOString(),
      city: 'Buffalo, NY',
      bands: 'The Forest Dwellers, The Others',
      desc: 'Super groovy show dog. Wow Holy moly!',
    },
    {
      title: 'Forest Dwellers A MYSTERY',
      venue: 'Nowhere',
      startDate: new Date().toISOString(),
      city: '?????!!?????',
      bands: 'The Forest Dwellers, ?????',
      desc: 'The most msyeterious show in the history of all shows! WHO EVEN KNOWS WHAT WILL HAPPEN? ',
    },
    {
      title: 'Forest Dwellers, Sugar Glider, RageChill',
      venue: 'UUU Art Collective',
      bands: 'Forest Dwellers, Sugar Glider, RageChill',
      startDate: new Date().toISOString(),
      desc: `
        really really really really really long
        long long description that talks a lot about
        the event and how fucking important it is
      `,
      city: 'Rochester, NY',
    },
    {
      title: 'Forest Dwellers + others',
      venue: 'Tabernacle',
      bands: 'The Forest Dwellers, The Others',
      startDate: new Date().toISOString(),
      desc: 'Super groovy show dog. Wow Holy moly!',
      city: 'Buffalo, NY',
    },
    {
      title: 'Forest Dwellers, Sugar Glider, RageChill',
      venue: 'UUU Art Collective',
      bands: 'Forest Dwellers, Sugar Glider, RageChill',
      startDate: new Date().toISOString(),
      desc: 'Super groovy show dog. Wow Holy moly! So many acts such wow.',
      city: 'Rochester, NY',
    },
    {
      title: 'Forest Dwellers + others',
      venue: 'Tabernacle',
      bands: 'The Forest Dwellers, The Others',
      startDate: new Date().toISOString(),
      desc: 'Super groovy show dog. Wow Holy moly!',
      city: 'Buffalo, NY',
    },
    {
      title: 'Forest Dwellers, Sugar Glider, RageChill',
      venue: 'UUU Art Collective',
      bands: 'Forest Dwellers, Sugar Glider, RageChill',
      startDate: new Date().toISOString(),
      desc: 'Super groovy show dog. Wow Holy moly! So many acts such wow.',
      city: 'Rochester, NY',
    },
  ];

  constructor() { }

  ngOnInit() {
  }

}
