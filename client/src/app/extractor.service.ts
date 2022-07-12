import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { lastValueFrom } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ExtractorService {

  constructor(private http: HttpClient) { }

  uploadFiles(files: File[]) {
    let formData = new FormData();
    files.forEach((file, index) => {
      formData.append('file', file);
    });
    lastValueFrom(this.http.post<any>(environment.serverDomain + '/file-upload', formData))
      .then((fulfilled) => {
        console.info(fulfilled);
      });
  }
}
