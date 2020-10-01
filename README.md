# Mira ☎️ (on Deta)

Mira is a personal contacts manager written by [Linus](https://github.com/thesephist/mira). It is a place for keeping in touch with people.

Mira is designed for quick actions and references to people I've met, and things I want to remember about those people. It looks like this in action:

![Mira on desktop](screenshot.png)

In particular, in addition to normal contact info you see in every app, Mira is capable of storing a few specific kinds of data I like to remember about people:

- past meetings ("mtg"): where are all the places I've met this person, in which occasion, and what did we talk about that I want to remember?
- last met ("last"): when did we last talk? This is useful when I want to follow up with people I haven't talked to in too long.
- place: what city do they live in? This is useful for remembering to visit people I haven't seen in a while whenever I visit a city for the first time in some time.
- unstructured notes: things like extracurricular or volunteering involvements, event attendance, hobbies, and other extraneous information that's useful to know, but not trivial.

This repo is modified to run on [Deta](https://www.deta.sh/). 


## Run on Deta

Deta provides a platform for hosting apps like Mira. Mira uses a Deta Micro and a Deta Base. Deta has built in authentication, only you can access your app and data.

To run your own Mira instance, follow these instructions:

- Get a [free account](https://www.deta.sh/)
- [Install the CLI](https://docs.deta.sh/docs/cli/install) and login
- Clone this repo and run `deta new`
- Click on the domain in the output