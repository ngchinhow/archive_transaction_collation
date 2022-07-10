import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {
  wrapperIsVisible: boolean = true;
  contentIsVisible: boolean = false;

  constructor() { }

  ngOnInit(): void {
  }

  readURL(event: any) {
    const files = event.target.files;
    if (files && files[0]) {

      var reader = new FileReader();

      reader.onload = () => {
        console.info(reader);
        this.wrapperIsVisible = false;

        var result = reader.result == null ? '' : reader.result.toString();
        document.getElementById('file-upload-image')?.setAttribute('src', result);
        console.log('reached here');
        this.contentIsVisible = true;
      };

      reader.readAsDataURL(files[0]);

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
  }

  mouseIn(div: string) {
    document.getElementById('image-upload-wrap')?.classList.add('image-dropping');
    console.log('mouse entered: ' + div);
  }

  mouseOut(div: string) {
    document.getElementById('image-upload-wrap')?.classList.remove('image-dropping');
    console.log('mouse leaved: ' + div);
  }
}
