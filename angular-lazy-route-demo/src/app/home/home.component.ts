import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  standalone: true,
  template: `
    <section>
      <h1>Angular 19 Lazy Route Demo</h1>
      <p>
        This is the eagerly loaded home page. Open the browser dev tools network tab and
        navigate to <strong>Reports</strong> to see the lazy chunk downloaded on demand.
      </p>
    </section>
  `
})
export class HomeComponent {}
