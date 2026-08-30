from fastapi import FastAPI
import httpx

app=FastAPI()
@app.get("/hello") #route 
def say_hello():
    return {"message": "Hello , world"}

@app.get("/add/{a}/{b}")
def Sum(a:int,b:int):
 return {"sum": a+b}



import httpx
@app.get("/github/{username}")
def get_github_user(username:str):
   response =httpx.get(f"https://api.github.com/users/{username}")
   data=response.json()

   return {"name": data["name"], "public_repos": data["public_repos"]}


import os
from dotenv import load_dotenv
load_dotenv()
my_token=os.getenv("GITHUB_TOKEN")

@app.get("/me")
def get_my_profile():
   headers={"Authorization": f"Bearer {my_token}"}
   response =httpx.get("https://api.github.com/user",headers=headers)
   data=response.json()
   return data

@app.get("/repo/{owner}/{repo}/pulls")
def github_call(owner:str,repo:str):
      headers= {"Authorization": f"Bearer{my_token}"}
      response= httpx.get(f"https://api.github.com/repos/{owner}/{repo}/pulls",headers=headers,follow_redirects=True)
      data= response.json()
      results=[]
      for pr in data:
         results.append({"number":pr["number"],"title": pr["title"]})
      return results
                         
@app.get("/repo/{owner}/{repo}/pulls/{pull_number}/files")
def git_pr_files(owner:str,repo:str,pull_number:int):
   headers={"Authorization": f"Bearer {my_token}"}
   response=httpx.get(f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files", headers=headers,follow_redirects=True)
   data=response.json()
   results=[]
   for file in data:
      results.append({
         "filename": file["filename"],
         "status": file["status"],
         "additions": file["additions"],
         "deletions": file["deletions"],
         "patch": file["patch"]
      })
   return results