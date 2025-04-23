import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardClientComponent } from './client/dashboard-client/dashboard-client.component';
import { CreateServiceComponent } from './client/create-service/create-service.component';
import { MyServicesComponent } from './client/my-services/my-services.component';

const routes: Routes = [
  {
    path: '',
    component: DashboardClientComponent,
    children: [
      { path: 'create-service', component: CreateServiceComponent },
      { path: 'my-services', component: MyServicesComponent },
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PagesRoutingModule { }
