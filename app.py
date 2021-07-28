from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def predict():
    # sentence = "do you use credit cards?"
    if request.method == 'GET':
        sentence = request.args.get('body')
        # print(sentence)
        # sentence = sentence['body']
        channels_list = []
        if sentence.lower() == 'technology':
            channels_list = ['#ask-looker', '#ask-optimization',
                             '#ask-programmatic-reporting', '#ask-pure',
                             '#ask-walled-gardens-platform',
                             '#askarchitecture'
                             '#customerorg-askanything']

            return jsonify({'response': channels_list})
        elif sentence.lower() == 'sports':
            channels_list = ['#sportsfanonly', '#eig-basketball',
                             '#eig-carrom'
                             '#eig-ches', '#eig-cricket']

            return jsonify({'response': channels_list})
        if sentence.lower() == 'travel':
            channels_list = ['#travel-stories', '#solo-traveller',
                             '#adventure']

            return jsonify({"response": channels_list})
        if sentence.lower() == 'team specific':
            channels_list = ['#ask-looker', '#ask-optimization',
                             '#ask-programmatic-reporting', '#ask-pure',
                             '#ask-walled-gardens-platform',
                             '#askarchitecture',
                             '#customerorg-askanything',
                             '#ias_viewability_skins']

            return jsonify({"response": channels_list})
        # if sentence == 'technology':
        #     channels_list = ['#ask-looker', '#ask-optimization',
        #                      '#ask-programmatic-reporting', '#ask-pure',
        #                      '#ask-walled-gardens-platform',
        #                      '#askarchitecture'
        #                      '#customerorg-askanything']
        #
        #     return jsonify({"response": channels_list})
        # if sentence == 'technology':
        #     channels_list = ['#ask-looker', '#ask-optimization',
        #                      '#ask-programmatic-reporting', '#ask-pure',
        #                      '#ask-walled-gardens-platform',
        #                      '#askarchitecture'
        #                      '#customerorg-askanything']
        #
        #     return jsonify({"response": channels_list})
        # if sentence == 'technology':
        #     channels_list = ['#ask-looker', '#ask-optimization',
        #                      '#ask-programmatic-reporting', '#ask-pure',
        #                      '#ask-walled-gardens-platform',
        #                      '#askarchitecture'
        #                      '#customerorg-askanything']
        #
        #     return jsonify({"response": channels_list})
        #
        # else:
        #     print(f"{bot_name}: I do not understand...")
        #     return jsonify({"response": ['I do not understand...']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
