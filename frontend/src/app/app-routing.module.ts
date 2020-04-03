import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LiveStreamFeedComponent } from './live-stream-feed/live-stream-feed.component';
import { WelcomeComponent } from './welcome/welcome.component';

const routes: Routes = [
  { path: 'streams', component: LiveStreamFeedComponent},
  { path: '', component: WelcomeComponent},
  { path: '**', component: LiveStreamFeedComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
