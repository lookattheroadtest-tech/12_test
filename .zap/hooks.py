def sending_request(request, initiator, message):
    try:
        if request.getMethod() == "POST":
            print("\n=== POST REQUEST ===")
            print("URL:", request.getURI())
            print("BODY:", request.getBody().toString())
    except:
        pass
