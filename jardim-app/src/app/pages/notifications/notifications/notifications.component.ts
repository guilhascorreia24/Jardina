import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-notifications',
  templateUrl: './notifications.component.html'
})
export class NotificationsComponent implements OnInit {
  notifications: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadNotifications();
  }

  loadNotifications() {
    this.http.get<any[]>('http://localhost:8000/notifications')
      .subscribe(data => this.notifications = data);
      for (let i = 0; i < this.notifications.length; i++) {
        console.log(this.notifications[i]);
      }
  }

  markAsRead(id: number) {
    this.http.post(`http://localhost:8000/notifications/read/${id}`, {})
      .subscribe(() => this.loadNotifications());
  }
}
