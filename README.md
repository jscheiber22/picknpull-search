## Purpose

The main purpose of this API is to automate a search for vehicles sitting in Pick N Pull lots around the world. It makes it far easier to setup a program to check every so often for new additions to these lots so you don't miss any parts or let it get ruined by rain.

---

## Using this API

To use the API in your own python file:
1. Import the class:
	from picknpull import PickNPull

2. Create an instance of the class with your vehicle's make and model
	pnp = PickNPull(model, startYear = None, endYear = None, zipcode = "95648", searchRadius = "50", verbose = False)
		-- model - current options include and are limited to: 
			-- "IS300"
			-- "WRX"
			-- "IMPREZA"
			-- "ACCORD"
		-- startYear - the first year to include in your search. Must also include an endYear
		-- endYear - the last year to include in your search. Must also include a startYear
		-- zipcode - the zip code to search around
		-- searchRadius - the radius around the zip code to search
		-- verbose - boolean to determine if print statements will print

3. Call the desired function:
	-- search() - returns count of vehicles found in radius as a string