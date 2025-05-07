import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardGardenerComponent } from './dashboard-gardener.component';

describe('DashboardGardenerComponent', () => {
  let component: DashboardGardenerComponent;
  let fixture: ComponentFixture<DashboardGardenerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DashboardGardenerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DashboardGardenerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
