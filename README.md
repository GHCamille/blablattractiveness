# Blablattractivity
Trying to compute the "attractivity" score of a city based on number of people going there during the weekend and what's the median price they are ready to pay for this. 

# How is this even relevant ?
It is : indeed as a Blablacar driver, I know myself that prices entered by drivers are based on what they think the passenger is ready to pay. The price need to be attractive because if it's not then the car is not full. For instance one might have 3 passengers for 10€ each while another will have 2 passengers for 12.5€ each. The first case is better for both the driver and the passengers. The only risk would be to have only 2 passengers, therefore second case would be better. But this case never happens. Why ? Well we notice that usually the cheapest trips are full. 

# Ok, fine, but what's the link with attractivity ?
I guess that we now agree in saying that the price does now depend on what passengers and drivers agree to be "worth the city". We can expect most of prices to be really cheap and then have some higher prices (prices suggested by the app, people trying the app for the first time, people who didn't check how much the competitors sell the trip). We will observe these KPIs : 

 - how many trips ?
 - how many people did this trip on Friday, 6:00 PM ?
 - how many people by car (average/median) ?
 - ratio nb-of-people/total-seats-in-the-car ? average/median
 - average/median price ?
 
 I think we can extract an attractivity score out of that. (to balance with the network the city has : is it remote (ex : Brest is kinda remote) ? is it well connected with tempting offers (like in Britanny people only pay 15€ when they are traveling less than 250km and are -26 years old) ?
 
 Let's see how this EDA goes. If it goes well with that first approach, I guess I'll extend it to other cities. 
