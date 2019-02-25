import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { EventListComponent } from './events/event-list/event-list.component';
import { CreateEventComponent } from './events/create-event/create-event.component';

const routes: Routes = [
  {path: '', component: EventListComponent},
  {path: 'create', component: CreateEventComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
