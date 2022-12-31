# [Architecture Assignment](https://app.diagrams.net/#Hshay79il%2FCloudArch%2Fmain%2FPizza_order.drawio)

## The Storyline - Pizza Order Website

We have a company that has a website for ordering Pizza.
The following are the different steps to order Pizza:

- The client is entering the website (pizza.hiredscore.com)
- The client decides what to order by browsing the different options
- The client sends the Order (Pay the bill, fill out the address and email & cellphone) to the website
- The client would get a notification (cellular & email) on his successful order
- After 1 hour the client gets the Pizza home

## Requirements

Define the architecture that can support the storyline above and the additional following requirements

## Website

- A website that would be able the serve 10s of thousands of concurrent users
- Website that can scale, since we might get peaks and the Mondial and other occasions

## Persistence

We would like to persist the user's Data as well as their order history.
Choose the Databases you would like to use for this data for easy querying(as well as scalability)

## Notifications

We would like to send a notification to the user
Define the pipeline to create the notifications

## Security

> Secure the site against DDOS Attacks

The site and Pizza have a lot of competition, and we suspect some malicious parties trying to harm the website.
You need to secure it!

> Authentication(bonus requirement)

The website can support accounts as well as guests, hence we would need to support authentication.
Authenticate users for login

---

---

# Code Assignment

```bash
kind create cluster --config kind-config.yaml
```

```docker
docker run -p 5000:5000 -d --name pizzaOrder shay79il/pizza
```
