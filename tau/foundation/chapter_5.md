### Future-proofing Test Automation

<br>

#### Design Considerations for Automation Tests

Knowing design considerations will help future-proof your automation project when it starts expanding to more tests.

##### Running in Parallel

When you have a handful of tests, running them sequentially isn't a bad idea. However, as the number of tests start to grow, it'll take longer for your test suite to complete. A solution to this problem is running tests in parallel.

You **should not have any tests dependent on one another**. They should be independent and **any setup or cleanup should be isolated within the test**. If so, you cannot run them parallel together.

_Objects and variables_ that are used in multiple tests should **be declared in a thread-safe manner** - meaning they _should not be global or static as their values could change_.
<br>

##### Clean Coding

Avoid excess code duplication, long classes and methods, inefficient waiting within tests, code smells, and other bad practices. Enable code reusability and maintainability.
<br>

##### Design Patterns

Design patters are beneficial for automation projects such as:

1. Page Object Model
2. Screenplay
3. Fluent
4. Builder
5. Singleton
6. Factory
7. Facade
