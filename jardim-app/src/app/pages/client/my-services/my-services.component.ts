import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-my-services',
  templateUrl: './my-services.component.html'
})
export class MyServicesComponent implements OnInit {
  services: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<any[]>('http://localhost:8000/services/my')
      .subscribe(data => this.services = data);
  }

  confirmService(id: number) {
    this.http.post(`http://localhost:8000/services/confirm_service/${id}`, {})
      .subscribe({
        next: () => alert('Serviço confirmado como concluído'),
        error: () => alert('Erro ao confirmar serviço')
      });
  }
}
