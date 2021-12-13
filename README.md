# Overview
URL Shortener was developed using this python.

It has two endpoint:

*  `/s/<string:url>/`: This receives a URL, then use a random hash to generate a shorter version and returns the shorten url to the caller
*  `/<id>` : This receives the shorten url and returns the original url

## Architecture
I attached two Architecture diagrams below.

The first shows what an ideal Architecture for this kind of api would be if it was to be designed and deployed in AWS. ECS, DynamoDB and API Gateway are all highly scalable, which will fulfil the scalability requirement that we had.

The second diagram shows the current arhcitecture which can be scaled using `docker compose scale`

![alt text](https://github.com/ayoolamakinde/sedna_uril/blob/main/arhictecture.png?raw=true)



## Tests

* Here is a test screnshot of the endpoint to shortened urls

![alt text](https://github.com/ayoolamakinde/sedna_uril/blob/main/shorten.png)

* Here is a test screnshot of the url redirect endpoint

![alt text](https://github.com/ayoolamakinde/sedna_uril/blob/main/redirect.png?raw=true)


## Alternate testing steps if docker-compose fails

Although, I have created both the docker and docker compose files, I didnt get a chance to test them because docker kept crashing on my personal computer and I didnt have the time to troubleshoot.

So, if you try running the docker compose and it fails for any reason please test using a virtualenv by following this steps.

* `pip3 install virtualenv`
* `cd api`
* `python3 -m venv . myenv`
* `source myenv/bin/activate`
* `pip install flask hashids`
* `python app.py`
* Then you can test both endpoints, try calling the endpoint to shorten the url, then try to call the end point for the redirct to validate it
