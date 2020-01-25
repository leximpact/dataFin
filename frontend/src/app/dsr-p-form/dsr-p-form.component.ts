import { Component, Output, EventEmitter, Input } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { VariablesDSR } from '../variables-dsr';

@Component({
  selector: 'app-dsr-p-form',
  templateUrl: './dsr-p-form.component.html',
  styleUrls: ['./dsr-p-form.component.css']
})
export class DsrPFormComponent {
  seuilHabitantsInitial = 10000;
  ponderationInitiale = 2;

  @Input() variables: VariablesDSR;
  @Output() simulate = new EventEmitter<void>();

  constructor(private fb: FormBuilder) {}

  onSubmit() {
    this.simulate.emit();
  }
}
