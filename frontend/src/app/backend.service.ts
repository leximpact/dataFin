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
    console.log(variables);
    // return this.http.post<{ communes: Communes }>('/dotations/dsr/eligebilite', variables).toPromise();
    return {
      communes: {
        eligibles: 5000,
        nouvelles: 45,
        anciennes: 22,
      }
    };
  }
}
