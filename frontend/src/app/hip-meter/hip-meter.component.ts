import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-hip-meter',
  templateUrl: './hip-meter.component.html',
  styleUrls: ['./hip-meter.component.sass']
})
export class HipMeterComponent implements OnInit {
  @Input() hipLevel: number;

  constructor() { }

  ngOnInit() {
  }

}
