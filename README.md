---
description: >-
  Democratizing the crypto knowledge is an api centric web application that
  brings knowledge in cryptocurrencies to regular people.
---

# 💻 Democratizing the crypto knowledge

## API Centric Web App

An API Centric Web Application is a web application that basically executes most, if not all, of its functionality through API calls.

At first, the web app obtains relevant information from pages such as CoinMarketCap. But in a second stage it is expected to consume other APIs, mostly from educational pages.

## APIs

For the development of the web app there will be used APIs.&#x20;

API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.

Both static information of the crypto and its latest listings will be the main endpoints consumed  through the CoinMarketCap API.&#x20;

For consuming the APIs it will be used the python language with the libraries requests and json. \
The request library in important because is the one who help the program to interact with the API. Nevertheless the json library is equally important because this is the data format of the endpoint response.

## Backend

For the backend development  Python was used. The library requests was essential to the program because allowed to this one to interact with the API and their exceptions. Moreover flask was used; a framework written in python that allows to create a web page.&#x20;

The code itself is divided in 4 functions; the first one is used to call both of the CoinMarketCap APIs endpoints; the second and third functions are used to manipulate the data; the fourth function is to dynamically create the web page.

The first function it's called call\_api and it's essentially used to interact with the API itself. \
This one gets two parameters,  called type and symbol. The first parameter is used for the program to know which endpoint to use, either the latest listing or the statistic information. The second parameter is used for consuming a specific crypto coin statistic information by its symbol, such as, BTC, ETH or ADA. &#x20;

The second function its called filtered data and has two parameters data and symbol. The importance of this function lies in consuming a dictionary from the latest listings endpoint and filtering the data with the symbol of the crypto coin (BTC, ETH, ADA, SOL).

The third function is called coin\_dictionary. The function is used for creating dictionaries with relevant info of specific coins, such as price, logo, slug, description, the source code and the websites.

For the fourth function its necessary to import flask and its dependencies.\
This function it's called html, and is the one responsible for consuming the API and interact with the frontend. The function itself do not get any parameters and the main purpose of this is to generates the dictionaries with the coin\_dictiornary function, to get the top 10 listings and render this info in the html web page.

## Frontend

The frontend was develop with a flask template. The flask template is written with jinja2 that allows to create a web page in a dynamical way using a html.\
This language also helps the communication between the backend and the web page.&#x20;

This development can eventually change with the opinion of a UX/UI expert that can put their knowledge of design and UX knowhow into practice.

## Improvements

The web app can possibly suffer some improvements in areas like the design of the webpage or the functionalities of this one. \
Also the app can consume more APIs and present more relevant information regarding to crypto knowledge.\
Further improvements will be made along new functionalities.

## Potential of the web app

The potential of this app lies in the adaptability to the CPA (Cost per action) or CPC (cost per click) business model where the app would offer different courses (consumed and present on screen with an API) and charge (commission or percentage) each time a user enters to the app or does a course.

## Extra documentation

Python: [https://docs.python.org/3/](https://docs.python.org/3/)

HTML: [https://docs.ckan.org/en/ckan-2.0/html-coding-standards.html](https://docs.ckan.org/en/ckan-2.0/html-coding-standards.html)

Flask: [https://flask.palletsprojects.com/en/2.0.x/](https://flask.palletsprojects.com/en/2.0.x/)&#x20;

Jinja2: [https://jinja.palletsprojects.com/en/3.0.x/](https://jinja.palletsprojects.com/en/3.0.x/)

CoinMarketCap: [https://coinmarketcap.com/api/documentation/v1/](https://coinmarketcap.com/api/documentation/v1/)
