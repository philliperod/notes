### Thought Experiment

```
Challenge: Starting from scratch, build and render the
HTML for our section project. Check the Google slide for
what you're trying to build.

We'll be adding styling to it later.

Hints:
* The React logo is a file in the project tree, so you can
  access it by using `src="./react-logo.png" in your image
  element
* You can also set the `width` attribute of the image element
  just like in HTML. In the slide, I have it set to 40px

// Completed but image is not showing up. Its alternate name shows up instead.
```

#### Quiz

> 1. **Why do we need to `import React from 'react'` in our files?**
>    So you can utilize JSX in your code. JSX is defined by React.
> 2. **If I were to console.log(component) in index.js, what would show up?**
>    Javascript objects. These are React elements that describe what React should eventually add to the real DOM for us.
> 3. **What's wrong with this code:**
>    It's not encapsulated in one `html` tag. Better way to say it - it needs to be in one parent element.
>
> ```
> const component = (
>   <h1>Hello</h1>
>   <p>This is my website</p>
> )
> ```
>
> 4. **What does it mean for something to be 'declarative' instead of 'imperative'?**
>    Tell me what to do and I will figure out how to do it. Imperative: tell me step-by-step what I need to do.
> 5. **What does it mean for something to be 'composable'?**
>    A collection of small codes that work together for something bigger.
