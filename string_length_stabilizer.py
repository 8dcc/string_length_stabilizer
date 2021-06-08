
test_id = "1234"
length_desired = 9

if len(test_id) < length_desired:  # If the desired length is less than the length of the actual id
	test_id = str(0)*(length_desired-len(test_id)) + test_id  # Add the ammount of ceros necesary to reach length_desired
	
	# Multiply str(0) because we want to add the digit, not multiply by cero. Multiply that
	# by the diference between lengths and then add the original id at the end

print(test_id)