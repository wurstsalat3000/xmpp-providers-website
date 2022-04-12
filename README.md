<!--
SPDX-FileCopyrightText: 2022 XMPP Providers Team

SPDX-License-Identifier: AGPL-3.0-or-later
-->

# XMPP Providers Website

[providers.xmpp.net](https://providers.xmpp.net) is a website generated based on data from the [XMPP Providers project](https://invent.kde.org/melvo/xmpp-providers).

## Software Requirements

* hugo
* python3

## Introduction to Hugo

Hugo’s [quickstart](https://gohugo.io/getting-started/quick-start/) page is a good place to learn about the basics of Hugo (installation, project skeleton, development cycle, etc.).

## Installation instructions

To run a development server on your local computer, follow these basic steps:

```bash
git clone https://github.com/xsf/xmpp-providers-website.git
# install Hugo
cd xmpp-providers-website
```

Running the server in development mode (reloads whenever a file is changed):

```bash
make serve
```

View at `http://localhost:1313`

## Deployment

```bash
docker build -t xmpp-providers -f ./Dockerfile .
docker run -p 80:80 -t -i xmpp-providers
```

## Theme development

This theme makes use of:

* [Bootstrap 5.1](https://getbootstrap.com/docs/5.1/)
* [FontAwesome 6](https://fontawesome.com/v6/docs/)
