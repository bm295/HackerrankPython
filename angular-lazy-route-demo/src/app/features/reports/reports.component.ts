import { Component } from '@angular/core';

@Component({
  selector: 'app-reports',
  standalone: true,
  template: `
    <section>
      <h2>Reports (Lazy Loaded)</h2>
      <p>
        You are now viewing content from a lazy-loaded route in Angular 19.
      </p>
    </section>
  `
})
export class ReportsComponent {}
