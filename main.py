from fastapi import FastAPI
import httpx

app=FastAPI()
import os
from dotenv import load_dotenv
load_dotenv()
my_token=os.getenv("GITHUB_TOKEN")

gemini_key=os.getenv("GEMINI_API_KEY")

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

@app.get("/ask-ai")
def call_gemini():
   url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={gemini_key}"
   body={
      "contents":[
         {
            "parts": [
                 {"text":  "Say hello in one sentence."}

            ]
         }
      ]
   
   }
   response=httpx.post(url,json=body, timeout=30)
   data=response.json()
   ai_text=data["candidates"][0]["content"]["parts"][0]["text"]
   return {"reply": ai_text}