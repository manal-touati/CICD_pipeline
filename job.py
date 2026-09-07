import os


a = 2 

print("coucou", a)


secret = os.environ.get("SECRET_API_TOKEN")
print("Secret bien récupéré" if secret else "Secret introuvable")
