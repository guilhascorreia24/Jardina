import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard-gardener',
  templateUrl: './dashboard-gardener.component.html'
})
export class DashboardGardenerComponent implements OnInit {
  services: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<any[]>('http://localhost:8000/services/my_pending_services')
      .subscribe(data => {
        this.services=data;
      });
  }

  markAsDone(serviceId: number) {
    this.http.post(`http://localhost:8000/services/confirm_service/${serviceId}`, {})
      .subscribe({
        next: () => {
          alert('Serviço marcado como concluído!');
          this.services = this.services.filter(s => s.id !== serviceId);
        },
        error: () => alert('Erro ao concluir serviço')
      });
  }
}
