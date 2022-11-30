### Designing for Test Automatability

<br>

#### Test Automation Pyramid

![](img/ch3_1.png)
<br>

##### Unit Level

At this level, you're designing automated tests close to production code which will provide _faster feedback_. These tests are called **unit tests**. The bulk of your automated tests will be written here and best written by developers as part of their feature development work (doesn't always happen). **Unit tests** are quick to write and execute. These are small modular test that **_verify the logic of individual functions without the need for integration_** of other functionality, DBs, or UI.
<br>

##### Services Level

Tests will focus on functionality that the code provides, but without a UI. These tests will make calls to APIs to verify integration of various individual functions. This will contain the second largest of automated tests.
<br>

##### UI Level

Furthest away from production code, tests will take longer to write and execute due to UI consistency. When considering a test here, determine what info the test needs to verify and choose the lowest level of the pyramid possible to write the test against.
<br>

---

### Example

<br>

#### Adding a Search Feature

A new search feature was created and you want to verify that searching for products does the following:

1. Return correct results.
2. Results appear as they should.
3. Other features working - filtering, sorting, column selection, pagination.

Automating multiple search tests can be costly at the UI level. Better option would be to automate one test at UI level and the rest at lower level. You already verified UI components and now you can test the functionality of the search algorithm at the service or unit level.
<br>

#### Adding Product to Shopping Cart

##### Test case:

1. Search for product.
2. Look through search results to find product.
3. Click on product.
4. Click "Add to Cart" button.
5. Click cart icon to get to cart.
6. Verify product is in cart.

Automating these steps at UI level is risky because any of those steps can fail when navigating the UI. At this point, you already added a UI level search test to your suite, so you can bypass the first scenario. What you're looking for are **seams**. Instead of searching for product, you can go to straight to the product's URL with your test, which will be your _seam_. You mitigate risk, lost time, and dependency of the search feature by removing those some steps. The test of adding product to the cart has no relation to the search feature. Adding the search test to this test would probably fail and block you from verifying the item in the cart.

**Seams:**
Shortcuts within the app that makes automating tests easier. Some are provided with the app by default:

1. _Unique URLs_ for various pages. This helps eliminate navigating the UI via meny items or various click streams.
2. _Web services_, provided by developers, allows you to bypass the UI and send quick HTTP requests to the app. These are great for pre-requisite setup, data verification, and cleaning up after test completion. Prime example of how developers can help with test automatability.
3. _Exposure to business functions_ which the test code can directly call the function that executes the action and bypass navigating through the UI. _The test needs access to the app's logic without the UI_. This is a **_service level automation_**.
   <br>

#### Verify Quantity of Product in Shopping Cart

##### Test case:

1. Search product.
2. Look through search results to find product.
3. Click on product.
4. Click "Add to Cart" button.
5. Click cart icon to get to cart.
6. Increase quantity of product in cart.
7. Verify count for product in cart.

Again, process of searching and adding product to the cart is not necessary at the UI level. By doing so, you add time, dependency, redundancy, and exposure to brittleness to your test.

Utilize a seam with web service call to add product to the cart, then go straight to the cart URL and begin your test. This method is faster and reduces risk of test failing.
<br>

##### UI Locators

For UI level tests, they will need to interact with the app by accessing its HTML elements. **A leading cause of flaky test is the absence/unreliable identifiers for HTML elements**.

It's important that developers add identifiers - _ID, name, or custom attribute_ - that is solely for test automation purposes when they create new web elements.
