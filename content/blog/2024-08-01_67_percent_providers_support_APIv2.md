---
title: Currently more than 50% of the listed XMPP providers support API version 2
date: 2024-09-01
---

Six months after we have offered the hosting a [generic JSON files](https://providers.xmpp.net/provider-file-generator/) which are based on our API version 2, more than [50% of the currently listed XMPP service providers](https://providers.xmpp.net/statistics/#provider-file) host it on their XMPP instance.
This is a great success for decentralization in XMPP onboarding. However, our efforts go beyond the project goals and chart a path to better transparency, quality and understanding of the entire XMPP network.

At the moment we have 72 XMPP providers listed in our setup.
By end of 2024 we want to exceed the 100.
Our main [statics](https://providers.xmpp.net/statistics/) shows that about 50% of the listed servers are categorized in D.
The main reasons are either closed registrations, missing information or both.
We recommend to also support the automated way we have established to not just support better onboarding, but also transparency of the network and general quality measures.

## Perspective &  Criticism

First of all, big thanks to all the supporters and applies of our projects and the helpful and constructive and last but not least welcome feedback.
Since we started about four years ago there have always been confronting criticism:
- Strong criticism on the rating
- Boycott of the service
- Abusive behavior
We do understand the main complains.
In this article I would like to invite you to take a very certain perspective: The users and newcomers to XMPP.

What do we know what they know?
What do we know what they understand?
The distances, between our highly tech-savvy knowledge and this of the majority of the users we often build our services and software for is huge.
And on the opposite, the tolerance of these people is often very thin.
Therefore, we should ensure a good experience right after registering to an XMPP server.

We have repeatedly discussed the minimum values of the rating parameters, the limits and the defined thresholds.
One example would be the effect of HTTP file upload parameters that are too low on the user experience.
Is 5 MB enough? Commonly sent videos can reach ten times that size, if not compressed.
Is this good? Is this something you as operator should care about?

Usually, to our understanding, most providers are also interested to have more users.
This is why we argued to have a minimum of 20 MB for example.
It is certainly not sufficient in all cases, but it will cover the commonly transferred sizes and ensures a better experience.
If you cannot or does not want to implement this, we recommend to not register newcomers with mainstream expectations on your server.
The users don't care about your properties, until they realize this video cannot be sent.
Then the chat client (!) and maybe even XMPP is blamed and they leave it.
The bitter truth is that public server maintainers have the potential to ruin the user experience and reputation of the network and also your XMPP applications.
Note to client developers: Users will regardless of the origin of the issue blame your chat app.

Due to the reality of the decentralized nature of the network, the discussions and the learnings required us to create more distinct and refined parameters.
The rating's main purpose is the recommendation for registration of especially non-tech-savvy newcomers to an XMPP server.

Ratings are sensitive and they obviously lead to conflict, no doubts.
Still, we took strong actions to keep it to deescalate and show good intentions.
- Keep the requirements for A as low as possible. We believe that even hobby-operators can easily meet these requirements if they want to.
- Actively reach out and help providers on their setup. And this lead to significant quality improvements in many setups, besides increasing their service rating.
- Host our support chat where we help operators even beyond the project with technical support with honorable improvements of their services.
- Offer a user-friendly, clearly documented and also semi-automated [XMPP Providers Server](https://invent.kde.org/melvo/xmpp-providers-server) with a good configured setup, written by Melvin.

## Vision

There are many XMPP chat client that help users to register a new account to a (pre-)existing list of XMPP server providers.
This is great and this is what the network nature should be.

However, there are two identified two issues, which lead to bad experiences:
- Varritation in quality of listed XMPP servers, due to often a manual maintained, outdated and uninformed nature
- Too restircitive behavior or no recommendation at all, that does not support the federated idea and leads to oligopoly-like distribution of users

We intend to address the problematic onboarding and user experience as well as promote user decentralization in XMPP through transparency, accessibility, quality and completeness of information.

As a control and evaluation service XMPP providers needs your trust. This is ensured by the following core characteristics:
- a service that keeps and supports a federated and decentralized interface
- a service that provides a transparent high level of even semi-automated and up-to-date information of listed servers with soft and hard quality measures
- a service tracks and enable quality checks overtime and even help operators with feedback to their service
- a service provides an API to automatically register a new account for a user
- a service that helps you as developer as well the user to retrieve service information and support contacts beyond the registration process

This is surely not a perfect solution to issues with registration and usability.
But it represents our strong efforts to improve the general unpopular situation around onboarding.
The priority is to prevent the two extremes:
- Unmaintained lists containing any server you can find and expose themselves in a lottery-manner to uninformed users to pick from.
- Purely limited selection of servers in your client that for sure may work, but unfortunately jeopardizes the idea of federation.

XMPP Providers with all the great achievements we have made so far is not the end of the road.
From a simple list for automatic registration we have evolved to build an API and a website with interesting statistics on the network.
We think that keeping up with good documentation and transparency is another great achievement.
We also wrote our own [automated setup](https://invent.kde.org/melvo/xmpp-providers-server) for everyone to have a good start.
We encourage you to use XMPP and run your own server instance, maybe even by becoming a public provider.
But keep in mind that providing a public service comes with great responsibility you should be aware of!

From this point we also believe that the project evolved to a multi-purpose project.
Thus, we propagate a prerequisite for smooth and sustainable registration process based on up-to-date information and the XMPP users in mind at your service.

That is not the one thing to solve and to improve.
Let’s make the best out of this project, regardless of how you apply to it.
We believe it is a great chance.
Remember, a rising tide lifts all boats.

## Outlook

We plan to expand our API with more measure and more way that you actually can expose the quality of your service, such as up-time and automated ways of confirming existing support.
But the project is nothing without usage. Gajim will soon publish their implementation of a new registration and on-boarding experience. Stay tuned!

If you got interested to list your service you can start with hosting a [generic JSON file](https://providers.xmpp.net/provider-file-generator/) and then create an issue, see section below.

Thank you for reading. We ask you to join this endeavor. Reach us in our support chat below.

— The XMPP Providers Team

## Help Us

For a good user experience, [apps integrating XMPP Providers](https://providers.xmpp.net/apps/) are as important as the providers themselves.
If you are an XMPP developer, please consider [adding XMPP Provider support](https://invent.kde.org/melvo/xmpp-providers#usage) to your app.
If you are an operator of a public XMPP service, provide the [information we need](/faq/#where-do-we-have-the-providers-properties-from) and [add it to our list](https://invent.kde.org/melvo/xmpp-providers/-/blob/master/CONTRIBUTING.md#providers).

Feel free to [reach out to us](/contact/) if you have any questions!

## Spread the Word

The XMPP Providers project lives from the community.
We are happy to hear your feedback!
[Follow us and spread the word](https://fosstodon.org/@xmpp_providers)!

{{< figure src="/images/xmpp-providers-adaptive.svg" caption="XMPP Providers Logo" class="text-center w-100 pt-5" height="300" link="/" >}}

