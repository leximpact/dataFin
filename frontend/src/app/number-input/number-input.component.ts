import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-number-input',
  templateUrl: './number-input.component.html',
  styleUrls: ['./number-input.component.css']
})
export class NumberInputComponent implements OnInit {
  @Input() initialValue: number;
  @Input() value: number;
  @Input() width: number;

  @Output() valueChange = new EventEmitter<number>();

  constructor() { }

  isModified(): boolean {
    return this.initialValue !== this.value;
  }

  ngOnInit() {
  }

}
