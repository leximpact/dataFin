import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-map-card',
  templateUrl: './map-card.component.html',
  styleUrls: ['./map-card.component.css']
})
export class MapCardComponent implements OnInit {
  @Input() path: string;

  constructor() { }

  ngOnInit() {
  }

}
