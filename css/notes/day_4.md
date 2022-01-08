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

> Just showing what it looks like when using `vw` for width.

![Image 1.3](../images/day4_6.png)
<br/>

The negative side of using `vh` or `vw` will be on mobile devices. Images or content inside a container can overlap outside its borders.

![Image 1.4](../images/day4_5.png)

To counter this, you will need to use media queries.
<br/>

> **Remember using percentages is based off of its parent's element.**

Using the Buy Now button's width, we will make it `100%` to show that it will be 100% of the width of its parent `<div class="col">`.

![Image 1.5](../images/day4_7.png)

Now, what if you use `vw` for its width? It will extend itself to the browser's screen size and put out the parent's content to the same width and pushing out any containers next to it as well.

![Image 1.6](../images/day4_8.png)

---

##### `vmax` and `vmin`
