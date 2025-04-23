import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-create-service',
  templateUrl: './create-service.component.html'
})
export class CreateServiceComponent {
  form = {
    description: '',
    address: '',
    gardener_id: 0
  };

  constructor(private http: HttpClient) {}

  onSubmit() {
    this.http.post('http://localhost:8000/services/create', this.form)
      .subscribe({
        next: () => alert('Serviço criado com sucesso!'),
        error: () => alert('Erro ao criar serviço')
      });
  }
}
