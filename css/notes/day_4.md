### CSS Units: `vh`, `vw`, `vmin`, `vmax`

- `vh` = viewport height
- `vw` = viewport width

![Image 1.0](../images/day4_2.png)
<br/>

In the above example, it is a two column hero container with a background image on the bottom.

**_One thing you should do initially that will help with your layouts is using_** `box-sizing: border-box` **_for the universal selector._** So, something like this:

```
* { // * means universal selector; selects everything
    box-sizing: border-box;
}
```

If you use `100vh` for the height in the hero container, it will extend the container to 100% of your "screen size" of the browser. If you were to change the size of the browser(shortening the browser for example), the hero container will dynamically change to that size.

![Image 1.1](../images/day4_3.png)
![Image 1.2](../images/day4_4.png)
<br/>

The negative side of using `vh` or `vw` will be on mobile devices. Images or content inside a container can overlap outside its borders.

![Image 1.3](../images/day4_5.png)
