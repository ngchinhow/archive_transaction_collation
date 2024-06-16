import { Component, OnInit } from '@angular/core';
import { ExtractorService } from '../services/extractor.service';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {
  wrapperIsVisible: boolean = true;
  contentIsVisible: boolean = false;
  files: File[] = [];

  constructor(private extractorService: ExtractorService) { }

  ngOnInit(): void {
  }

  readURL(event: any) {
    const files: FileList = event.target.files;
    if (files) {
      this.files = Array.from(files);
      this.wrapperIsVisible = false;
      this.contentIsVisible = true;
    } else {
      this.removeUpload();
    }
  }

  removeUpload() {
    let uploadInput = document.getElementById('file-upload-input');
    if (uploadInput) {
      uploadInput.replaceWith(uploadInput.cloneNode());
    }
    this.contentIsVisible = false;
    this.wrapperIsVisible = true;
    this.files = [];
  }

  uploadData() {
    this.extractorService.uploadFiles(this.files);
  }

  mouseIn(div: string) {
    document.getElementById('image-upload-wrap')?.classList.add('image-dropping');
    console.info('mouse entered: ' + div);
  }

  mouseOut(div: string) {
    document.getElementById('image-upload-wrap')?.classList.remove('image-dropping');
    console.info('mouse leaved: ' + div);
  }
}
