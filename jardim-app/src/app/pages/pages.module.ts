import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PagesRoutingModule } from './pages-routing.module';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { DashboardClientComponent } from './client/dashboard-client/dashboard-client.component';
import { CreateServiceComponent } from './client/create-service/create-service.component';
import { MyServicesComponent } from './client/my-services/my-services.component';


@NgModule({
  declarations: [
    LoginComponent,
    RegisterComponent,
    DashboardComponent,
    DashboardClientComponent,
    CreateServiceComponent,
    MyServicesComponent
  ],
  imports: [
    CommonModule,
    PagesRoutingModule
  ]
})
export class PagesModule { }
