import { Component } from '@angular/core';
import { AuthService } from 'src/app/core/services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html'
})
export class RegisterComponent {
  form = {
    name: '',
    email: '',
    password: '',
    is_gardener: false
  };

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService.register(this.form).subscribe({
      next: () => this.router.navigate(['/auth/login']),
      error: () => alert('Erro no registo')
    });
  }
}
