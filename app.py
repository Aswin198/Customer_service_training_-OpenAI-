from flask import Flask, render_template, request
from scenarios import SCENARIOS
from evaluator import eval
from models import get_db_connection, init_db
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/scenario/<int:scenario_id>", methods=["GET", "POST"])
def show_scenario(scenario_id):
    temp = None

    for i in SCENARIOS:
        if i["id"] == scenario_id:
            temp = i
            break

    if temp is None:
        return "Scenario not found", 404

    if request.method == "POST":
        user_response = request.form.get("user_response")
        feedback = eval(temp["email"], user_response)
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO attempts (
                    scenario_id,
                    scenario_title,
                    user_response,
                    overall_score,
                    strengths,
                    improvements,
                    suggested_reply
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
        temp["id"], temp["title"], user_response, feedback["overall_score"], " | ".join(feedback["strengths"]),
        " | ".join(feedback["improvements"]), feedback["suggested_reply"]))

        conn.commit()
        conn.close()

        return render_template(
            "result.html",
            scenario=temp,
            user_response=user_response,
            feedback=feedback
        )
    return render_template("scenario.html", scenario=temp)

@app.route("/dashboard")
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attempts ORDER BY id DESC")
    attempts = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", attempts=attempts)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

