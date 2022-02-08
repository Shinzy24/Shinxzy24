if __name__ == "__main__":
	try:
		__import__("app").make()
	except Exception as e:
		exit(str(e))
