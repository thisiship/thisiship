import { Component, Input } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { EventDialogComponent } from '../event-dialog/event-dialog.component';

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.sass']
})
export class EventComponent {
  @Input() title: string;
  @Input() venue: string;
  @Input() startDate: string;
  @Input() city: string;
  @Input() bands: string;
  @Input() desc: string;
  @Input() price: number;
  // @Input() hipMeter: number;
  /*
    hipMeter idea -
    could have a little icon on each event progressing from cold to hot
    ice cube - water - .... - fire
  */

  constructor(public dialog: MatDialog) {}

  openDialog() {
    this.dialog.open(EventDialogComponent, {
      width: '80%',
      height: '80%',
      data: {
        title: this.title,
        venue: this.venue,
        startDate: this.startDate,
        city: this.city,
        bands: this.bands,
        desc: this.desc,
        price: this.price,
      },
    });
  }
}
