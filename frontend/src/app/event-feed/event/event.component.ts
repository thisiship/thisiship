import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.sass']
})
export class EventComponent implements OnInit {
  @Input() title: string;
  @Input() venue: string;
  @Input() bands: string;
  @Input() desc: string;
  @Input() startDate: string;
  @Input() city: string;
  // @Input() hipMeter: number;
  /*
    hipMeter idea -
    could have a little icon on each event progressing from cold to hot
    ice cube - water - .... - fire
  */

  constructor() {}

  ngOnInit() {
  }

}
