import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MaterialModule } from './material.module';
import { HeaderComponent } from './header/header.component';
import { EventFeedComponent } from './event-feed/event-feed.component';
import { EventComponent } from './event-feed/event/event.component';
import { EventDialogComponent } from './event-feed/event-dialog/event-dialog.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { AboutComponent } from './about/about.component';
import { HipMeterComponent } from './hip-meter/hip-meter.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    EventFeedComponent,
    EventComponent,
    EventDialogComponent,
    NotFoundComponent,
    AboutComponent,
    HipMeterComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MaterialModule,
    BrowserAnimationsModule
  ],

  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
