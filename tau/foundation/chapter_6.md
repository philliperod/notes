### Scaling Your Test Automation

<br>

Considerations that you need to take when scaling your automation projects to run in multiple environments, browsers, and/or devices.
<br>

#### Multiple Environments

Different environments may have different information - such as IP addresses or URLs, login credentials, and DB info. It's best to extract these sort of details for your project and make use of artifacts like _properties files_.

With the use of **properties files**, you can focus on the content of the test vs coding multiple conditional paths. Burden with managing test data and other artifacts needed for test automation can be mitigated through _containerization_.
<br>

#### Cross-browser

Determine if testing a few select browsers will suffice rather than testing all browsers.
<br>

#### Multiple Devices

Nowadays, users tend to access apps from all types of devices. Are you creating and maintaining a device farm or using a cloud based service for your devices? Also, do your UI level tests work when your app is in responsive layout?

Some elements are replaced with mobile-friendly ones and your test code should handle that, such as native mobile apps like iOS and Android. Can your test suite run on both or you need to create two different suites to support each?
