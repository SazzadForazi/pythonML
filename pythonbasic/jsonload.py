import json
# x =  '{ "name":"John", "age":30,"city":"New York" }'

# x='[{"id": "tt0096895","name": "Adiba islam","review": "Excellent laptop and service. Arrived quickly. Would have liked a next day delivery option though. Only complaint.","Rating": "8.00"}]'
x = {
"id": "tt0096895",
"name": "Adiba islam",
"review": "Excellent laptop and service. Arrived quickly. Would have liked a next day delivery option though. Only complaint.",
"Rating": "8.00"
},
{
"id": "tt0468569",
"name": "Rakib Hasan",
"review": "delivery quick and easy but did not know that the graphics no good with windows 10 so disappointed with that.",
"Rating": "9.00"
},
{
"id": "tt2975590",
"name": "MR. leo",
"review": "Disappointed. I bought the Refurbished Acer Aspire XC-895 Core i5-10400 8GB 1TB Windows 10 Desktop to replace my laptop but it is slower than my laptop.",
"Rating": "9.00"
},
{
"id": "tt1345836",
"name": "Samsul Hoque",
"review": "Everything done really quickly and all working well.",
"Rating": "10.00"
},
{
"id": "tt0372784",
"name": "Rahim Uddin",
"review": "Returning customer and got the same fabulous service. Will use again.",
"Rating": "9.50"
},
{
"id": "tt4116284",
"name": "Karim Hossen",
"review": "Other than the box about beaten up the laptop inside was fine.",
"Rating": "7.00"
}
    
# y = json.loads(x)
y=json.dumps(x)
print(y)
