import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EventFeedComponent } from './event-feed/event-feed.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { AboutComponent } from './about/about.component';


const routes: Routes = [
  { path: 'about', component: AboutComponent, },
  { path: 'event-feed', component: EventFeedComponent, },
  { path: '', redirectTo: 'event-feed', pathMatch: 'full'},
  { path: '**', component: NotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
