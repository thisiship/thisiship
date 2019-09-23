import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';
import { ProfileModel } from '../profile/profile.model';

@Injectable({ providedIn: 'root' })
export class HomeService {
  profiles: ProfileModel[];
  profileSub = new Subject<ProfileModel[]>();

  constructor(private http: HttpClient) {}

  fetchProfiles() {
    this.http.get<ProfileModel[]>(`http://localhost:3000/profile`)
      .subscribe(response => {
        this.profiles = response;
        this.profileSub.next(this.profiles);
      });
  }

}
