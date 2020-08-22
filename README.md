
# 🚗 Blablattractiveness  📈
The objective of the project is to compute a KPI that demonstrates how attractive a city is for travelers. 

# How is this even relevant ?
It is : indeed as a Blablacar driver, I know myself that prices entered by drivers are based on what they think the passenger is ready to pay. The price need to be attractive because if it's not then the car is not full. For instance one might have 3 passengers for 10€ each while another will have 2 passengers for 12.5€ each. The first case is better for both the driver and the passengers. The only risk would be to have only 2 passengers, therefore second case would be better. But this case never happens. Why ? Well we notice that usually the cheapest trips are full. 

# Ok, fine, but what's the link with attractivity ?
I guess that we now agree in saying that the price does now depend on what passengers and drivers agree to be "the worth of the city". 
We can expect a price distribution that goes with most of the prices really cheap, and then have some higher prices, that are usually mistakes (prices suggested by the app, people trying the app for the first time, people who didn't check how much the competitors sell the trip, so they put the price far too expensive). Usually mistakes result in people don't booking the trip. We will study the following metrics to build our KPI : 

 - how many trips ? (by date)
 -  what is the average/median price ? (by date)
 - what is the prices distribution ? (all time)
<!--- - how many people did this trip on Friday, 6:00 PM ?
 - how many people by car (average/median) ? 
 - ratio nb-of-people/total-seats-in-the-car ? average/median -->

 Let's see how this EDA goes. 

# Let's go
We will build a database of routes and keep track of all trips and their prices for a month.


# First Steps
1) ✅ Get API.
2) ✅ Build the architecture.
3) ✅  Write the code for one route only.
3) ✅ Integrate in the architecture, and test the CRON.
4) ✅ Build a list of all the routes we will study.
2) 🔁 See how it goes - Want to query for trips ID for Rennes > Brest Fridays 6:00PM if possible
3) For each trip - same origin same destination same hour : what's the price ?
4) Compute median/average price
5) See the results ... How does it go ?

# Build the architecture
For now we have : 

![Architecture GCP](https://github.com/GHCamille/blablattractivity/blob/master/Pictures/GoogleCloudArc.png)

# What's next ?

Our results will be really biased, in a way that it will not enable us to compare cities. There are far too many biases (like how connected the city is : is it connected to a train line ? plane ? how expensive is it to have a car in that city : is the parking ticket expensive ? is fuel expensive ?). It could be interesting to build a KPI that get us rid of these biases. But that would be for another study.
That KPI aims at helping cities see their attractiveness evolution : are they getting more attractive with time ?
 
