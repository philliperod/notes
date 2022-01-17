### First React Project

![Image 1.0](../images/info_1.png)

Adding these React `<script>` allows the dev to start using the React library for their project via CDN.

The first `<script>` pulls in the react library and the second `<script>` is react dom, but just these two scripts are very limited to utilize React itself. `ReactDOM` is a script that renders everything on the screen. To use it fully, you need to pull in the `<script>` for Babel.

![Image 1.1](../images/info_2.png)

This will allow you to use JSX in any `<script>` tag by adding `type="text/babel"`

You can use `ReactDOM` script gives you access to the global variable, `ReactDOM`, in the javascript file which will render something on the screen. This will render code that looks like `html`.
<br/>

#### Example:

![Image 1.2](../images/info_3.png)

A basically template that has the 3 `<script>` tags from above (2 that pulls the React library and renders your code; last one that allows you to use JSX). In the example, you can see the `<h1>` tag that says "Hello, React".

To show how `ReactDOM` can render your code, you'll remove the `<h1>` tag in the `html` file and put it in the javascript file using `ReactDOM`. This will showcase how React can help create declarative code.

##### How ReactDOM

`ReactDOM` has two inputs needed - what do you want to render onto the screen, where do you want to render it.

In the example above, you'll remove the `<h1>` tag from the `html` file and replace it with a `<div id="root">`. The `ReactDOM` code in the javascript file will replace this.
