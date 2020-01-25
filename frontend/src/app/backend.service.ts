import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { VariablesDSR } from './variables-dsr';
import { Communes } from './communes';

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  constructor(private http: HttpClient) { }

  async simulate(variables: VariablesDSR): Promise<{ communes: Communes }> {
    return this.http.post<{ communes: Communes }>('http://localhost:5000/dotations/dsr/eligebilite', variables).toPromise();
  }
}
