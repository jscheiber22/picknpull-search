<b>Purpose</b>

The main purpose of this API is to automate a search for vehicles sitting in Pick N Pull lots around the world. It makes it far easier to setup a program to check every so often for new additions to these lots so you don't miss any parts or let it get ruined by rain.

<hr>

<b>Using this API</b>

To use the API in your own python file:<br>
1. Import the class:<br>
	from picknpull import PickNPull<br>
2. Create an instance of the class with your vehicle's make and model<br>
	pnp = PickNPull(model, startYear = None, endYear = None, zipcode = "95648", searchRadius = "50", verbose = False)<br>
		-- model - current options include and are limited to: <br>
			-- "IS300"<br>
			-- "WRX"<br>
			-- "IMPREZA"<br>
			-- "ACCORD"<br>
		-- startYear - the first year to include in your search. Must also include an endYear<br>
		-- endYear - the last year to include in your search. Must also include a startYear<br>
		-- zipcode - the zip code to search around<br>
		-- searchRadius - the radius around the zip code to search<br>
		-- verbose - boolean to determine if print statements will print<br>
<br>
3. Call the desired function:<br>
	-- search() - returns count of vehicles found in radius as a string<br>