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




@app.get("/review/{owner}/{repo}/pulls/{pull_number}")
def review_pr(owner: str, repo: str, pull_number: int):
   headers = {"Authorization": f"Bearer {my_token}"}
   response = httpx.get(
       f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files",
       headers=headers,
       follow_redirects=True
   )
   data = response.json()
   all_reviews=[]
   for file in data:
      filename = file["filename"]
      patch = file["patch"]

      prompt_text = f"""You are a senior code reviewer. Review the following code change and point out any bugs, security issues, or code quality problems. Be concise.

Filename: {filename}

Diff:
{patch}"""

      url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={gemini_key}"
      body = {
         "contents": [
            {
               "parts": [
                   {"text": prompt_text}
               ]
            }
         ]
      }
      ai_response = httpx.post(url, json=body, timeout=30)
      ai_data = ai_response.json()
      if "candidates" not in ai_data:
        ai_text= "AI review unavailable right now (rate limit or API error). Please try again later."
      else:
        ai_text = ai_data["candidates"][0]["content"]["parts"][0]["text"]
   
      comment_body_text = f"**Review for `{filename}`:**\n\n{ai_text}"
      comment_headers={"Authorization": f"Bearer {my_token}"}
      comment_url=f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments"
      comment_body={"body": comment_body_text }
      comment_response = httpx.post(comment_url,headers=comment_headers, json=comment_body)
      all_reviews.append({
         "filename": filename,
         "review": ai_text,
         "comment_status": comment_response.status_code
   
      })
   return all_reviews
      
      # return {"filename": filename, "review": ai_text}
   # all_reviews.append({"filename": filename,"review": ai_text})
   # return all_reviewscomment_



@app.get("/post-comment/{owner}/{repo}/{pull_number}")
def post_comment(owner: str, repo: str, pull_number: int):
    headers = {"Authorization": f"Bearer {my_token}"}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pull_number}/comments"
    body = {"body": "This is a test comment from my AI review bot."}
    response = httpx.post(url, headers=headers, json=body)
    return {"status_code": response.status_code, "raw_text": response.text}


@app.get("/check-token")
def check_token():
    if my_token:
        return {"token_preview": my_token[:40] + "..."}
    else:
        return {"status": "Token not loaded"}