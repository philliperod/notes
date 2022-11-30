### Automation Test Tooling

<br>

For your automation test project, you need an _interaction tool_ and _validation tool_.

**Interaction**
For unit tests and service tests that call into production functions, it should be written in the same programming language as production code.

For the other tests, you have more flexibility. Service tests that call into APIs need to execute HTTP requests and read through responses. Search for programming languages or libraries that makes it easy.

For UI tests, a navigation library that provides the ability to interact with HTML elements. You can use a tool that supports the same programming language, but better to find a tool focuses on browser and device support.
<br>

**Validation**
Validation libraries that turn your code into a pass/fail test that verifies functional, visual, accessibility, security, etc.
