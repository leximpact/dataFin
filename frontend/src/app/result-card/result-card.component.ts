import { Component, OnInit, Input } from '@angular/core';
import { Communes } from '../communes';

@Component({
  selector: 'app-result-card',
  templateUrl: './result-card.component.html',
  styleUrls: ['./result-card.component.css']
})
export class ResultCardComponent implements OnInit {
  @Input() communes: Communes | 'pending' | 'failure' | null = null;

  constructor() { }

  ngOnInit() {
  }

}
