from flask import Flask
from src import status

app = Flask(__name__)

COUNTERS = {}


# We will use the app decorator and create a route called slash counters.
# Specify the variable in route <name>.
# Let Flask know that the only method that is allowed to be called
# on this function is "POST".
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter."""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT

    # If the counter doesn't exist, create it with a value of 0.
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """Update a counter."""
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        # If the counter exists, increment it by 1.
        COUNTERS[name] += 1
        return {name: COUNTERS[name]}, status.HTTP_200_OK


@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    """Read a counter."""
    app.logger.info(f"Request to read counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {name: COUNTERS[name]}, status.HTTP_200_OK

@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """Delete a counter."""
    app.logger.info(f"Request to delete counter: {name}")
    global COUNTERS6
    if name in COUNTERS:
        COUNTERS.pop(name)
        return {name: name}, status.HTTP_204_NO_CONTENT
