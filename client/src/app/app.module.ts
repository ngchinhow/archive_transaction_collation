import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FileUploadComponent } from './file-upload/file-upload.component';
import { ExtractorService } from './services/extractor.service';
import { FolderComponent } from './folder/folder.component';

@NgModule({
  declarations: [
    AppComponent,
    FileUploadComponent,
    FolderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [ExtractorService],
  bootstrap: [AppComponent]
})
export class AppModule { }
