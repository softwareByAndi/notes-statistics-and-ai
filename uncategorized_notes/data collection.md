---
tags:
  - "#statistics"
links:
  - "[[hypothesis testing]]"
---
# interesting notes

in the mammogram example, the treatment offered group was split into 2, those who accepted and those who didn't. I was tempted to just compare those who accepted, but it turns out that that would create a bias, because the people who declined treatment turned out to be a very different group from the group that accepted, so comparing only 1 group would actually **remove randomness** from the trial... Also, given that the trial was testing whether **offering** a mammogram would reduce deaths, and that the plan to be implemented would be optional, it turns out to be important to compare the entire treatment set as a whole.
- It should also be considered that comparing accepted v.s. refused groups would create difficult to discern results due to the [[latent variables]] that influenced the people in each group to accept or refuse, such as education level, location/environment, financial situation, ethnicity/culture, etc... It would, therefore, be difficult to determine how much the analysis results would be influenced by *(very likely)* non-random, latent variables.
- #study-question this has something to do with the [[problem of confounding]]... but what is that?

# controlled randomized experiment
EVERYTHING that is not what you care about should be RANDOMIZED. otherwise the data might reflect the effects of another constant, which may be unrelated to the dependent [[Datum Features|feature]] that you're interested in.
- e.g. are these results & or variation due to the people doing the test, or due to the test itself... etc...