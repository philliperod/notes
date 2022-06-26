### How To Answer Estimation Questions

Tech companies are infamous for asking seemingly ridiculous “estimation questions,” also known as **Fermi Problems**. These questions are common in case interviews, software engineering interviews, and especially, product management interviews.

How is a PM interviewee supposed to answer this question? Are you expected to come up with a reasonable final number? Is there a particular strategy the interviewer is seeking? Below is a common structure that applies to most great estimation interview responses, as well as our three estimation question lessons.

---

#### 1. Memorize Basic Facts

It’s helpful to have these numbers in mind to bound your answer with reasonable estimates, and most of the time, these basic facts will help in your solution. Try to assess what industry the company works in and gather basic facts with numbers.

- US population: 330M
- California population: 40M
- NYC population: 8M
- World population: 7.8B
- Size of continental US: 3M square miles
- US households: 130M
- Average people per household in the US: 3
- Life expectancy: 72
- Median household income: $65,000
- Weight of an average car: 4000lbs
  <br/>

##### Technical

- Amazon S3 Standard cost: $0.023 / GB / month
- Average file size for a 90-min 720p movie: roughly 3.5GB
- Average file size for a smartphone camera picture: roughly 3-5 MB
- Average CTR for a search ad: 1.91%
- Average landing page conversion rate: 2.35%
- Average WiFi bandwidth: ~10Mbps
- Cost of iPhone 12 Pro: $999
- Cost of Google Pixel 5: $699
- Cost of Amazon Echo (4th Gen): $99
  <br/>

##### General sense of revenue (2020)

- Dropbox revenue: $2B
- Airbnb revenue: $3B
- Google revenue: $181B
- Facebook revenue: $86B
- Apple revenue: $274B
- Amazon revenue: $386B
- Netflix revenue: $25B
- Google (Alphabet) net income: $40.27 billion
- Apple R&D expenditure: $18.75 billion
  <br/>

##### General sense of user populations

- Netflix (Q2 2021): 209 million subscribers
- Google G Suite (March 2020): 2 billion+ monthly active users
- Uber (Jun 2021): ~1 million drivers in the US
- Twitter (Q1 2018): 192 million daily active users
- Number of Americans that own a smart speaker (Jan 2020): 60 million
- Number of products Amazon sells: over 12 million (not including Amazon marketplace sellers, which brings the total to 350 million)

Don’t over-memorize. You’ll just need to know a few basics to ground your answer. It’s not impressive for you to memorize the answers to all possible interview questions. This interview question tests how you think, not the final answer.

---

#### 2. Scope The Problems

Ask questions to clarify the scope of the problem in question.

Example: interviewer asks you to estimate the weight of a schoolbus.

- Does the weight estimate include a full tank of gas?
- Does the weight estimate include humans inside the schoolbus?
- How many people is the schoolbus expected to seat in total?

Interviewer may respond by telling you to make assumptions as needed.

---

#### 3. Break Down The Problem

It’s critical to explain your structure prior to answering. Specifically, how will you go about breaking down the problem into component pieces so that the problem becomes more tractable?

Example (cont. from above about the schoolbus): **_we isolate each component of a schoolbus and estimate its contribution to the overall weight._**

- Metal Exterior
- Engine
- Gas Tank (especially if full)
- Tires
- Interior (seats, driving wheel, etc.)
- External accessories (mirrors, lights, etc.)

Now that you've broken down the problem (and the schoolbus), you can estimate the individual weight of each piece.

##### Estimate the number of miles of road in continental US

Already memorized there are 3M square miles of land in the US. The approach will be to estimate the road density for a square mile of the US.

> Given a square mile of the US, how much road is in it?

You can break down this problem into rural and urban square miles as road density will differ between the two.

---

#### 4. Estimate

So far, you have broken the problem, considered exceptions, and explain your approach. Now, the numbers.

> Interviewer do not care what the actual numbers are.

##### Estimate the number of miles of road in the US

Now, you need to calculate the road density of a square mile. Imagine a square mile of the US, and, on average, across cities and rural areas. You can probably guess that there might be 2 miles of road per square mile. Why?

Reasonable to think that there's a road crossing across both the length and height of the square mile. In rural areas, there may be no roads at all, but in cities and small towns, there will be more roads. On average, this could be a fair estimate.

---

#### 5. Answer

After estimating various components, provide your answer. Usually, this requires plugging all our mini-estimates into our larger equation and summing the total.

---

#### 6. Tell Your Interviewer Why You're Wrong

Your answer will be wrong. Tell your interviewer if, based on a quick gut check, you think your answer is an overestimate or underestimate. Explain what factors you would consider if you had more time. What elements did you ignore because you didn't forsee them to factor significantly in the calculation? This helps anticipate your interviewer's qualms with your answer.

---

### Estimation Questions Strategies and Tricks

Estimation questions are open-ended. It can be hard to explain your process or do quick whiteboard math. Below are some strategies to counteract those problems.
<br>

#### Estimating the Unknowns

Most estimation questions will ask you to estimate something you have no clue about. For example, "how many cars are there in Seattle?"

##### 1. Estimate via proxy

An excellent method to estimate a number is to figure out another related and known number. Instead of trying to guess how many cars in Seattle, we can hypothesize that the number of cars is directly related to the number of familes in the area. This latter quantity is easier to derive a number for.

Once you have the relative quantity, all you need to do is scale up or down. For example, if we assume there are 300k households in Seattle, it doesn't mean there are 300k cars. Each household may have, on average, 2 cars. So, that means there are 300k \* 2 cars = 600k cars in Seattle.

##### 2. Personal references

In essense, what any method to estimate is trying to do is related some unknown quantity to some known quantity and move from there. One fail-safe option is to relate the unknown quantity to some known quantity in your life. From there, you can adjust your assumptions when necessary.

##### 3. Upper and lower bounds

When all else fails, start with extremes. What's the realistic upper and lower limit of quantity X? You can whittle down these limits through the course of the interview, ending in a much narrower range or concrete number.

For example, the extreme lower limit of cars in Seattle is 0 and the extremem upper limit is probably the population size of Seattle - around 1 million. If you take the average of the two numbers, you get 500k cars in Seattle. The actual number is closer to 430k. But, in the interview, we don't care about the correctness as much as we care about your process. So, whittle down the range with revelant assumptions.

---

#### Math Tricks

You can apply a few simple strategies to turn hard mental math problems into quick and painless whiteboard answers.

##### 1. Rounding Numbers

Estimation questions are looking for ballpark figure and not accurate answers. If you have an inconvenient number, **ROUND IT**. **_Take some number and round it to the some power of 10_**.

> Be sure to communicate to the interviewer that you are rounding the figure. State it out loud.
>
> **Examples**:
> 7.6 billion becomes 8 billion or 10 billion
> 237 million becomes 200 million

##### 2. Split Your Multiplications

Even after rounding, multiplying big numbers can be hard. Here's an example:

> What is 70 million times 40?
>
> 70,000,000 x 40 = (7 x 10,000,000) x (4 x 10) = (7 x 4 x 10,000,000 x 10) = (28 x 100,000,000) = **2.8 billion**
>
> What is 15% of 70?
> 15% of 70 = (10% of 70) + (5% of 70) = (0.1 x 70) + (0.05 x 70) = 7 + (0.5 x 0.1 x 70) = 7 + 3.5 = **10.5**

The trick is to multiply the non-power-of-10 numbers together first, then multiply that result with all powers of 10. Additionally, numbers can be split up into sums that are easier to work with. Lastly, dividing/multiplying by 10 and 2 are the simplest divisions, so try to get your numbers in multiples of those two numbers.

##### 3. Dealing with Power of 10

Remember that multiplying by a power of 10 is moving the decimal place over.
