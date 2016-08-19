def FizzBuzz(numero):
	if numero == 15:
		return "fizzbuzz"

	if not numero % 3:
		return "fizz"

	if not numero % 5:
		return "buzz"

	return numero