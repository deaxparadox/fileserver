import { Routes } from '@angular/router';
import { HomeComponent } from './component/home/home.component';
import { UploadComponent } from './component/upload/upload.component';

export const routes: Routes = [
    {
        path: "home",
        component: HomeComponent
    },
    {
        path: "u",
        component: UploadComponent
    }
];
