
# 🚗 Blablattractiveness  📈
The objective of the project is to compute a KPI that demonstrates how attractive a city is for travelers. 

# How is this even relevant ?
It is : indeed as a Blablacar driver, I know myself that prices entered by drivers are based on what they think the passenger is ready to pay. The price need to be attractive because if it's not then the car is not full. For instance one might have 3 passengers for 10€ each while another will have 2 passengers for 12.5€ each. The first case is better for both the driver and the passengers. The only risk would be to have only 2 passengers, therefore second case would be better. But this case never happens. Why ? Well we notice that usually the cheapest trips are full. 

# Ok, fine, but what's the link with attractiveness ?
I guess that we now agree in saying that the price does now depend on what passengers and drivers agree to be "the worth of the city". 
We can expect a price distribution that goes with most of the prices really cheap, and then have some higher prices, that are usually mistakes (prices suggested by the app, people trying the app for the first time, people who didn't check how much the competitors sell the trip, so they put the price far too expensive). Usually mistakes result in people don't booking the trip. We will study the following metrics to build our KPI : 

 - how many trips ? (by date)
 -  what is the average/median price ? (by date)
 - what is the prices distribution ? (all time)
<!--- - how many people did this trip on Friday, 6:00 PM ?
 - how many people by car (average/median) ? 
 - ratio nb-of-people/total-seats-in-the-car ? average/median -->

I think that combining can be a good starting point to building this KPI. Let's see how the EDA goes.

# Let's go
We will build a database of routes and keep track of all trips and their prices for a month.

At first, I wanted to query the Blablacar API to check which routes are the busiest. But that wasn't possible, because the API requires the origin and the destination to be cities. After some research, still impossible to get the data. So I decided to create my own map, based on the top 25 cities in France.

I cannot study every city because I have a limit of 1000 queries per day to Blablacar, and then I also have a trickier limit to follow on Google Cloud Functions. Therefore I will build routes from these 25 cities from and EDA. 

We will do a first study to select the routes we will choose between those 25 cities.

<!-- If the number of trips on a route is inferior to the first quartile of the number of trips to the destination, I will not study this route. -->

We chose the top 25 cities. It means we have 15 511 210 043 330 985 984 000 000  possible routes. We will do a selection of the major routes.

# First Steps
1) ✅ Get API.
2) ✅ Build the architecture.
3) ✅  Write the code for one route only.
4) ✅ Integrate in the architecture, and test the CRON.
5) ✅ Build a list of all the routes we will study.

Ressources : [1](https://blog.blablacar.fr/newsroom/news/blablacar-lance-blablabus-a-destination-de-45-villes-en-france), [2](https://blog.blablacar.fr/newsroom/news/blablacar-et-ouibus-s-associent-pour-repondre-a-la-forte-demande-pendant-la-greve), [3](https://blog.blablacar.fr/newsroom/news/blablacar-reunit-un-demi-million-de-covoitureurs-depuis-debut-juin-et-relance-ses-blablabus)

[IN PROGRESS] Code for routes selection.

6) ❌ Data collection in a bucket. (1 month)
7) ❌ Study the results : statistics on dataset. (✅ code ready)
8) ❌ See the results ... How does it go ?

# Build the architecture
For now we have : 

![Architecture GCP](https://github.com/GHCamille/blablattractivity/blob/master/Pictures/GoogleCloudArc.png)


# What's next ?
Our results will be really biased, in a way that it will not enable us to compare cities. There are far too many biases (like how connected the city is : is it connected to a train line ? plane ? how expensive is it to have a car in that city : is the parking ticket expensive ? is fuel expensive ?). It could be interesting to build a KPI that get us rid of these biases. But that would be for another study.

The KPI we built has to be tracked over time, city by city.

This study gave me ideas to compute an ecofriendliness KPI. Indeed, Blablacar is an ecofriendly mean of transport. Number of trips by Blablacar can be a useful data to study how ecofriendly the population living in a city is. 
This study will be more complicated, I will have to gather other sources of data. 

[A good place to start this new study.](https://blog.blablacar.fr/blablalife/lp/zeroemptyseats)

 
