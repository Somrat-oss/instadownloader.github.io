import instaloader

ig = instaloader.Instaloader()

req_user = input("req user name ")
username = input("enter user name")
password = input("enter password")
ig.login(username,password)
ig.download_profile(req_user,download_stories=True)