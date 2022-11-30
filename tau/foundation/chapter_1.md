### Designing Testing Automation Strategy

<br>

#### Common Goals

1. Reducing time for regression testing.
2. Reducing technical debt.
3. Enable continuous testing as part of build process.
   <br>

#### Planning Execution

##### Which tests to automate?

Strategic planning is necessary to factor risk and value for automation testing. Not all tests should be automated because of **time and maintenance**.
<br>

##### What's the scenario?

Actions and expected results may be defined via acceptance tests, Gherkin scenarios, or test cases.
<br>

##### What about implementation?

What kind of tooling being used to test - programming languages, frameworks.
<br>

##### How will the tests be executed?

Think about when and how these tests will be executed. Start from top phase to transition to others.

1. Someone test and report results = requires manual intervention (slow) but results is already triaged and accurate.
2. Execute multiple times a day within CI = faster feedback but results not triaged, proficient tests.
3. Integrated with development = fast and reliable tests that only fails when app under test provokes it.
   <br>

##### Triaging and Maintaining Automated Tests

It's best to realize test failures will need to triaged and maintained, and plan for. Plan accordingly. Ideally, any tests that fail will be due to their changes, and therefore code can be fix or update the test to reflect new expectations of the app.
