# ISA_Marketing_Platform
Marketing platform

Uses django built in user fyi
Removed csrf token for any post routes to simplify testing for TA's

API Routes:

```


GET /api/v1/users Gets all the buyers
POST /api/v1/user/create/?   Creates a buyer
POST /api/v1/user/update/?   Updates a buyer
DELETE /api/v1/user/delete/?   Deletes a buyer

GET /api/v1/ad  Gets all the ads
POST /api/v1/ad/create/?  Creates an ad
POST /api/v1/ad/update/?  Updates a specific ad
DELETE /api/v1/ad/delete/?  Deletes a specific ad

GET /api/v1/buyer Gets all the buyers
POST /api/v1/buyer/create/?   Creates a buyer
POST /api/v1/buyer/update/?   Updates a buyer
DELETE /api/v1/buyer/delete/?   Deletes a buyer

GET /api/v1/seller  Gets all the sellers
POST /api/v1/seller/create/?  Creates a seller object
POST /api/v1/seller/update/?  Updates a seller object
DELETE /api/v1/seller/delete/?  Deletes a seller object

```


# Individual Route Info

## POST /api/v1/user/create/?  Creates an user


###### params 
name (name of user) <br />
email  (unique email of user) <br />
password  (password of user) <br />

## DELETE /api/v1/user/delete/?  Delete an user


###### params 
pk (pk of user) <br />



## POST /api/v1/user/update/?  Updates a specific user


###### notes
Cant update pk associated with user <br /> 
Update as many fields as you want <br /> 
pk is *required* <br /> 
any other values in the query will be the newest values for the user <br /> 

###### params
pk (integer of the pk of the user) <br />
name (url of an online image) <br />
password (new password of user)  <br />
email  (new email of user) <br />



## POST /api/v1/ad/create/?  Creates an ad


###### params 
user  (integer of a user pk) <br />
image (url of an online image) <br />
url (url of a website) <br />
site_title  (title of ad) <br />
duration  (integer of how long ad will last) <br />
cost  (cost of ad)



## POST /api/v1/ad/update/?  Updates a specific ad


###### notes
Cant update user associated with ad <br />
Update as many as you want <br />
pk is *required* <br />


###### params
pk (integer of the pk of the ad) <br />
image (url of an online image) <br />
url (url of a website)  <br />
site_title  (title of ad) <br />
duration  (integer of how long ad will last) <br />
cost  (cost of ad) 

## DELETE /api/v1/ad/delete/?  Deletes a specific ad


###### params
pk (integer of the pk of the ad)


## POST /api/v1/buyer/create/?   Creates a buyer


###### params
user (integer of user pk) <br />
credit (integer of how much credit the user has)


## POST /api/v1/buyer/update/?   Updates a buyer


###### params
credit (integer of credit)

##### notes
Can't change user associated with the buyer



## DELETE /api/v1/buyer/delete/?   Deletes a buyer

###### params
pk (integer of user pk)

##### notes
pk is *required*


## POST /api/v1/seller/create/?  Creates a seller object

###### params
company (string of company of the seller) <br />
user (integer of user pk)


## POST /api/v1/seller/update/?  Updates a seller object

###### params
company (string of company of the seller)

###### notes
Can't change user associated with seller

## DELETE /api/v1/seller/delete/?  Deletes a seller object

###### params
pk (integer of user pk)

###### notes
pk is *required*

