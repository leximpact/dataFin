import { Component } from '@angular/core';
import { Communes } from './communes';
import { VariablesDSR } from './variables-dsr';
import { BackendService } from './backend.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  communes: Communes | 'pending' | 'failure' | null = null;

  variables: VariablesDSR = {
    seuilHabitants: 10000,
    ponderation: 2
  };

  constructor(private backend: BackendService) {}

  async simulate() {
    try {
      this.communes = 'pending';
      const { communes } =  await this.backend.simulate(this.variables);
      this.communes = communes;
    } catch (error) {
      this.communes = 'failure';
    }
  }
}