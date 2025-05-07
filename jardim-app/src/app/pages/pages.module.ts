import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PagesRoutingModule } from './pages-routing.module';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { DashboardClientComponent } from './client/dashboard-client/dashboard-client.component';
import { CreateServiceComponent } from './client/create-service/create-service.component';
import { MyServicesComponent } from './client/my-services/my-services.component';
import { DashboardGardenerComponent } from './gardener/dashboard-gardener/dashboard-gardener.component';
import { NotificationsComponent } from './notifications/notifications/notifications.component';
import { LOCALE_ID } from '@angular/core';
import localePt from '@angular/common/locales/pt';
import { registerLocaleData } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';

registerLocaleData(localePt);

@NgModule({
  declarations: [
    LoginComponent,
    RegisterComponent,
    DashboardComponent,
    DashboardClientComponent,
    CreateServiceComponent,
    MyServicesComponent,
    DashboardGardenerComponent,
    NotificationsComponent,
  ],
  imports: [
    PagesRoutingModule,
    CommonModule,
  ],
  providers: [{ provide: LOCALE_ID, useValue: 'pt' }]
})
export class PagesModule { }
