from flask import Flask, request, jsonify
import util
app=Flask(__name__)

@app.route('/location')
def get_location():
    response= jsonify({
        'location_names' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
    print("Starting project")
    print(get_location())
    app.run()