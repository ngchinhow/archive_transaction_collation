import { v4 as uuidv4 } from 'uuid';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-folder',
  templateUrl: './folder.component.html',
  styleUrls: ['./folder.component.css']
})
export class FolderComponent implements OnInit {
  folders: Folder[] = [];

  constructor() { }

  ngOnInit(): void {
  }

}
