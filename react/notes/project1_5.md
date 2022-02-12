### Custom Components Cont...

Quiz!

1. What is a React component?
   A reusable function that returns React elements.
2. What's wrong with this code?
   There is no parent element like `<div>` or `<>`. I was wrong - it's missing the capitalization on the first letter of the function (myComponent > MyComponent).

```
function myComponent() {
    return (
        <small>I'm tiny text!</small>
    )
}
```

3. What's wrong with this code?
   In ReactDOM.render, the first parameter should not be a function but rather `'<Header />'`.

```
function Header() {
    return (
        <header>
            <nav>
                <img src="./react-logo.png" width="40px" />
            </nav>
        </header>
    )
}

ReactDOM.render(Header(), document.getElementById("root"))
```
