from flask import Flask, render_template, request
from openai import OpenAI
app = Flask(__name__)
client=OpenAI(base_url="https://openrouter.ai/api/v1",api_key="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")


@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""
    role= """
You are a University FAQ Assistant helping students with university-related queries.
Provide accurate, concise, and student-friendly answers about admissions, courses, fees, exams, and campus facilities.
"""

    if request.method == "POST":
        prompt = request.form["prompt"]

        response =client.chat.completions.create(model="openrouter/free",messages=[{"role":"user","content":f" your role :{role},user input : {prompt}"}])

        response_text = response.choices[0].message.content

    return render_template(
        "index.html",
        message=response_text
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
