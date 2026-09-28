


def binary_to_decimal(binary: str) -> int:
	"""Convert a string containing only binary digits to a decimal integer."""
	if not binary or any(digit not in "01" for digit in binary):
		raise ValueError("binary input must contain only 0 and 1")
	return int(binary, 2)


def decimal_to_binary(decimal: int) -> str:
	
	if decimal < 0:
		raise ValueError("decimal input must be non-negative")
	return bin(decimal)[2:]


def main() -> None:

	choice = input("Choose conversion (1: binary to decimal, 2: decimal to binary): ").strip()

	try:
		if choice == "1":
			binary_input = input("Enter a binary number: ").strip()
			print(f"Decimal: {binary_to_decimal(binary_input)}")
		elif choice == "2":
			decimal_input = input("Enter a non-negative decimal number: ").strip()
			print(f"Binary: {decimal_to_binary(int(decimal_input))}")
		else:
			print("Invalid choice. Enter 1 or 2.")
	except ValueError as error:
		print(f"Invalid number: {error}")


if __name__ == "__main__":
	main()