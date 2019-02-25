import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

import { EventsService } from '../events.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create-event',
  templateUrl: './create-event.component.html',
  styleUrls: ['./create-event.component.css']
})
export class CreateEventComponent implements OnInit {
  @ViewChild('f') form: NgForm;

  constructor(private eventsService: EventsService,
    private router: Router) { }

  ngOnInit() {
  }

  onSubmit() {
    const value = this.form.value;
    const newEvent = {
      title: value.title,
      description: value.description,
      startDate: `${value.startDate} ${value.startTime}` ,
      endDate: `${value.endDate} ${value.endTime}`,
      price: value.price
    };
    this.eventsService.addEvent(newEvent);
    this.router.navigate(['']);
  }

}
