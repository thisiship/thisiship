import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';
import { ProfileModel } from './profile.model';

@Injectable({ providedIn: 'root' })
export class ProfileService {
  profile: ProfileModel;
  profileSub = new Subject<ProfileModel>();

  constructor(private http: HttpClient) {}

  fetchProfile(username: string) {
    this.http.get<ProfileModel[]>(`http://localhost:3000/profile/${username}`)
      .subscribe(response => {
        this.profile = response[0];
        this.profileSub.next(this.profile);
      });
  }

}
