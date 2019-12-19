import json
from flask import Flask, render_template, request
app = Flask(__name__)
#e41008f5070e4c1ca83f54fff2b456ce
@app.route('/')
def home():

    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
	headers = {'Authorization': 'Key <e41008f5070e4c1ca83f54fff2b456ce>'}
    image_url = request.form['url-input']
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response_dict = json.loads(response.content)


    return render_template('home.html', results=response_dict)

if __name__ == '__main__':
    app.run(debug=True)