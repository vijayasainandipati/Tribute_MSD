from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    hero_name = "Mahendra Singh Dhoni"
    hero_image_url = "https://wallpaperaccess.com/full/1281432.jpg"
    hero_description = "Captain Cool."
    hero_achievements = [
        "MS Dhoni is the only Indian captain who has led India to all three major ICC events. From winning the maiden T20 World Cup in 2007 on his captaincy debut to lead India to a World Cup victory on home soil in 2011. In 2013 he has won the Champions Trophy",
        "Under his captaincy, India holds the numero uno position in Test ranking for 18 months",
        "On November 1, 2011, the Indian Territorial Army conferred with honorary rank Lieutenant Colonel to Dhoni after which Dhoni has become the only captain after Kapil Dev to receive this prestigious award"
    ]
    return render_template('index.html', hero_name=hero_name, hero_image_url=hero_image_url, hero_description=hero_description, hero_achievements=hero_achievements)

if __name__ == '__main__':
    app.run(debug=True)
