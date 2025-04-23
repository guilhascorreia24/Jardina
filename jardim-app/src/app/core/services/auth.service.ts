import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { BehaviorSubject, tap } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private baseUrl = 'http://localhost:8000/auth';
  private tokenSubject = new BehaviorSubject<string | null>(null);

  constructor(private http: HttpClient) {}

  login(data: { email: string; password: string }) {
    const body = new HttpParams()
      .set('username', data.email)
      .set('password', data.password);
  
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded'
    });
  
    return this.http.post<any>(`${this.baseUrl}/login`, body.toString(), { headers }).pipe(
      tap(response => {
        localStorage.setItem('token', response.access_token);
        this.tokenSubject.next(response.access_token);
      })
    );
  }

  register(data: any) {
    return this.http.post(`${this.baseUrl}/register`, data);
  }

  getToken() {
    return this.tokenSubject.value || localStorage.getItem('token');
  }
}
