import newrelic.agent

newrelic.agent.initialize('newrelic.ini')

# Set custom attribute


from flask import Flask

app = Flask("MyFlaskApp")

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Hello world</h1>"

if __name__ == '__main__':
    app.run()
#k