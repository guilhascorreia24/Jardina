import { RouterModule, Routes } from '@angular/router';
import { MainLayoutComponent } from './layout/main-layout/main-layout.component';
import { LoginComponent } from './pages/auth/login/login.component';
import { RegisterComponent } from './pages/auth/register/register.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { NgModule } from '@angular/core';
import { DashboardGardenerComponent } from './pages/gardener/dashboard-gardener/dashboard-gardener.component';
import { NotificationsComponent } from './pages/notifications/notifications/notifications.component';
import { DashboardClientComponent } from './pages/client/dashboard-client/dashboard-client.component';
const routes: Routes = [
  {
    path: '',
    component: MainLayoutComponent,
    children: [
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
      { path: 'dashboard', component: DashboardComponent },
      { path: 'auth/login', component: LoginComponent },
      { path: 'auth/register', component: RegisterComponent },
      { path: 'gardener/dashboard', component: DashboardGardenerComponent },
      { path: 'notifications',component: NotificationsComponent},
      { path: 'client/dashboard', component: DashboardClientComponent },

    ],
  },
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {} 
