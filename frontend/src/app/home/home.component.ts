import { Component, OnInit } from '@angular/core';
import { HomeService } from './home.service';
import { ProfileModel } from '../profile/profile.model';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.sass']
})
export class HomeComponent implements OnInit {
  profiles: ProfileModel[] = [];
  profilesSub: Subscription;

  constructor(private homeService: HomeService) { }

  ngOnInit() {
    this.profilesSub = this.homeService.profileSub.subscribe(profiles => {
      this.profiles = profiles;
    });
    this.homeService.fetchProfiles();
  }

}
