import { Component, afterRender, afterNextRender, ElementRef } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HomeComponent } from './component/home/home.component';
import { NavbarComponent } from './layout/navbar/navbar.component';
import { FooterComponent } from './layout/footer/footer.component';
import { UploadComponent } from './component/upload/upload.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    HomeComponent,
    NavbarComponent,
    FooterComponent,
    UploadComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  private mainHeight: string = "null";


  constructor(elementref: ElementRef) {
    afterRender(() => {
      const main = elementref.nativeElement.querySelector(".ewl-main") as HTMLDivElement;
      // main.style.height
      console.log(main.clientHeight, document.body.clientHeight)
      if (main.clientHeight < document.body.clientHeight) {
        main.style.height = `${document.body.clientHeight.toString()}px`;
      }
    })

  }

  title = 'appui';


}
