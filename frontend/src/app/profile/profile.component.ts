import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { ProfileModel } from './profile.model';
import { ProfileService } from './profile.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.sass']
})
export class ProfileComponent implements OnInit {
  profile: ProfileModel;
  profileSub: Subscription;

  constructor(
    private route: ActivatedRoute,
    private profileService: ProfileService
  ) {
    this.route.params.subscribe(params => {
      if (params.username) {
        this.profileService.fetchProfile(params.username);
      }
    });
  }

  ngOnInit() {
    this.profileSub = this.profileService.profileSub.subscribe(profile => {
      this.profile = profile;
    });
  }
}
