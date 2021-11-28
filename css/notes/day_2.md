### Day Two - Getting Familiar With Relative Units

<br/>

#### Why You Shouldn't Set `font-size` Using `em`

1. Using `em` in `font-size` can cause a compounding effect within the content of that `element`.
2. So, they will look for their parent's `font-size` and compound that value.

![Image 1.0](../dayTwo_1.png)
![Image 1.2](../dayTwo_2.png)
![Image 1.3](../dayTwo_3.png)

<br/>
<br/>

**_Example: call-to-action item_**

```
// HTML code

<div class="cta">
    <h2 class="cta__title">Buy our product</h2>
    <p class="cta__body">Lorem, ipsum...</p>
    <p>
        <a href="#" class="cta__btn">Buy now</a>
    </p>
</div>


// CSS Code

.cta {
    font-size: 1.2em;
}

.cta__title {
    margin: 0 0 0.5em;
}

.cta__btn {
    display: inline-block;
    padding: 0.5em 1.5em;
    font-size: 1.25em;
}
```

![Image 2.2](../dayTwo_4.png)
<br/>
<br/>

1. If you were to add `font-size` to `cta__title` or `cta__body` or `cta__btn`, then they will compound their value to their parent's, `cta`, `font-size` creating oversizing within that parent element.
   - `cta__btn` is also within a `p` element so it will be compounding that element first then compound the `cta` parent element

```

// HTML code

<div class="cta">
    <h2 class="cta__title">Buy our product</h2>
    <p class="cta__body">Lorem, ipsum...</p>
    <p>
        <a href="#" class="cta__btn">Buy now</a>
    </p>
</div>


// CSS code

.cta {
    font-size: 1.2em;
}

.cta__title {
    margin: 0 0 0.5em;
    font-size: 3em; // 19px (1.2em) * 3em = 57px
}

.cta__body {
    font-size: 1.25em; // 19px (1.2em) * 1.25em = 24px
}

p {
    font-size: 1.125em;
}

.cta__btn {  // this is also compounding its parent 'p'
    padding: 0.5em 1.5em;
    font-size: 1.25em; // 18px (1.125em) * 1.25em = 22.5px * 1.2em = 27px
}
```

![Image 2.1](../dayTwo_6.png)
![Image 2.2](../dayTwo_5.png)
![Image 2.3](../dayTwo_7.png)
<br/>
<br/>

2. Now, if you were to use `rem` in `font-size` then it becomes more reasonable to handle as it will look for the `root`'s `font-size` value (typically `<html>` tag which defaults to `font-size: 16px`).

```
.cta {
    font-size: 1.2rem; // 16px * 1.2rem = 19px
}

.cta__title {
    margin: 0 0 0.5em; // 0 0 0.5em * 48px = 0 0 24px
    font-size: 3rem; // 16px * 3rem = 48px
}

.cta__body {
    font-size: 1.25rem; // 16px * 1.25rem = 20px
}

p {
    font-size: 1.125rem; // 16px * 1.125rem = 18px
}

.cta__btn {
    padding: 0.5em 1.5em; // 0.5em 1.5em * 20px = 10px 30px
    font-size: 1.25rem; // 16px * 1.25rem = 20px
}
```

![Image 2.4](../dayTwo_8.png)
<br/>

3. This also illustrates that using `em` is great for `margin`, `padding`, or the like because it is referencing the element's own `font-size`.
   - if you were to change the value of the element's `font-size` then the `margin` or `padding` using the `em` value will auto-scale to it.

![Image 2.5](../dayTwo_9.png)
![Image 2.6](../dayTwo_10.png)
<br/>

4. If you were to use `rem` for `margin` or `padding`, then it's like setting a set value since it will reference to the `root` which defaults to `16px`.
   - Regardless if you were to increase the value of the element's `font-size`, it will remain a static sizing to its own.

![Image 3.0](../dayTwo_11.png)
![Image 3.1](../dayTwo_12.png)
![Image 3.2](../dayTwo_13.png)
<br/>

5. If you were to use `em` for `margin` or `padding`, then it will scale appropriately to its element's `font-size`.
   - It keeps its consistent.

![Image 4.0](../dayTwo_14.png)
![Image 4.1](../dayTwo_15.png)
<br/>
<br/>

_*Additional Note*:_

Using `rem` when changing the `font-size` across the board, you are referencing the `root`.

And if using `@media (max-width: num_px)` for different viewport sizes, it can change all of the `font-size` at once rather than listing each element that needs to be changed.
