## Dependencies

You must download these for the application to work successfully.
1. selenium
2. subprocess

---

## Using the API

To use the API in your own python file:
1. Import the class:
	from picknpull import PickNPull
2. Create an instance of the class with your vehicle's make and model
	pnp = PickNPull(make, model, zipcode = "95648", searchRadius = "50")
3. Call the desired function:
	-- search() - returns count of vehicles found in radius