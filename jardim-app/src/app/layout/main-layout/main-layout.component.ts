import { Component } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-main-layout',
  templateUrl: './main-layout.component.html',
  styleUrls: ['./main-layout.component.scss']
})
export class MainLayoutComponent {
  isGardener = false;
  unreadCount = 0;
  constructor(private http: HttpClient) {}
  ngOnInit() {
    this.isGardener = localStorage.getItem('isGardener') === 'true';
    this.http.get<any[]>('http://localhost:8000/notifications')
    .subscribe(data => {
      this.unreadCount = data.filter(n => !n.read).length;
    });
  }
  
}
