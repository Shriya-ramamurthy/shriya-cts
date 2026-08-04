import { Component } from '@angular/core';

@Component({
selector:'app-root',
template:`

<h1>{{title}}</h1>

<input [(ngModel)]="title">

<br><br>

<a routerLink="/">Home</a>

|

<a routerLink="/about">About</a>

<router-outlet></router-outlet>

`
})

export class AppComponent{

title="Angular Demo";

}