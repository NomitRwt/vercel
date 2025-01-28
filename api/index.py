from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Data
students = [{"name":"lkxLBUYnGI","marks":99},{"name":"5AN","marks":55},{"name":"Q6z2PH","marks":49},{"name":"IrZnXN5nO","marks":3},{"name":"oBx","marks":77},{"name":"G47j","marks":64},{"name":"FWqvyr","marks":26},{"name":"qByVn","marks":17},{"name":"tZQCtp3cde","marks":41},{"name":"W6UC","marks":8},{"name":"xbaDwukw","marks":48},{"name":"7Muq","marks":70},{"name":"PoQrAvCf","marks":37},{"name":"Zc","marks":55},{"name":"dqt205Qd","marks":66},{"name":"66m41","marks":7},{"name":"Rl5BGxsDgX","marks":59},{"name":"I","marks":48},{"name":"1iu1WceKy","marks":50},{"name":"dY5Ooma","marks":46},{"name":"ug8V","marks":86},{"name":"7ccENTVa","marks":3},{"name":"AFCXW","marks":25},{"name":"YAlZ1","marks":55},{"name":"1bnzyLvROB","marks":20},{"name":"JqiSgSz","marks":13},{"name":"n3","marks":85},{"name":"dOQEJ1j2","marks":97},{"name":"uaXuWLf9","marks":6},{"name":"jA","marks":99},{"name":"ydmrF","marks":92},{"name":"OxBlngO","marks":99},{"name":"7pVQujqy","marks":58},{"name":"oNh","marks":34},{"name":"68tjYN","marks":92},{"name":"9fi7tk","marks":62},{"name":"KZJHfe4A","marks":74},{"name":"Mbks","marks":15},{"name":"3QJ","marks":97},{"name":"x8KmGeGaR","marks":37},{"name":"aOlJ0dyE","marks":6},{"name":"RkjQhqkfkJ","marks":21},{"name":"MQ8yyzYKYg","marks":11},{"name":"3iq7h","marks":12},{"name":"hHgbq","marks":48},{"name":"QmYVLSdJei","marks":55},{"name":"trtWGEJp0o","marks":92},{"name":"MA0zM7g","marks":58},{"name":"PAuY6nW6","marks":29},{"name":"FOWjqpn","marks":29},{"name":"Ltlv","marks":87},{"name":"J","marks":58},{"name":"m5WkxJfP","marks":61},{"name":"1LgoCDEmD2","marks":76},{"name":"hj","marks":25},{"name":"7d0oFF1gNN","marks":92},{"name":"uvA","marks":72},{"name":"DEFIR","marks":87},{"name":"xoYCqO5i","marks":69},{"name":"eyfKFK2Jt","marks":76},{"name":"XA2","marks":88},{"name":"EYFphgdSf","marks":54},{"name":"jv3","marks":8},{"name":"av","marks":54},{"name":"7II15lJB","marks":93},{"name":"Dh","marks":82},{"name":"OwH3GQU","marks":67},{"name":"bJY","marks":48},{"name":"uc","marks":5},{"name":"H4q","marks":90},{"name":"3AJVGr","marks":73},{"name":"zmK","marks":83},{"name":"lCT6D3jy9q","marks":57},{"name":"b2cMi","marks":88},{"name":"eRnJxy85","marks":61},{"name":"cBNW96","marks":20},{"name":"OIywYQr9p","marks":8},{"name":"KglV5N2","marks":34},{"name":"LFS7ydsX","marks":86},{"name":"Ymna","marks":7},{"name":"rdcHLhBoBt","marks":28},{"name":"Urbi4","marks":30},{"name":"nQ","marks":36},{"name":"bfFku4Q1nk","marks":74},{"name":"i1BEpG","marks":53},{"name":"JxaO0VXL","marks":90},{"name":"vU5uhafRp","marks":3},{"name":"DZoDCxCQ","marks":20},{"name":"6i7y","marks":2},{"name":"QeWRj7P","marks":61},{"name":"e6XcBZ","marks":85},{"name":"dT9q15FkIu","marks":9},{"name":"1aDf","marks":94},{"name":"TyWmLrNxe","marks":23},{"name":"33xRD","marks":72},{"name":"H0","marks":69},{"name":"A50vNe","marks":81},{"name":"0","marks":2},{"name":"j0txbGhk","marks":57},{"name":"H8Scr","marks":16}]

@app.route("/api", methods=["GET"])
def get_marks():
    # Get 'name' parameters from the query
    names = request.args.getlist("name")
    print(names)
    
    # Create a dictionary for quick lookup of marks by name
    student_marks = {student["name"]: student["marks"] for student in students}
    
    # Preserve the order of names as in the query
    marks = [student_marks.get(name, None) for name in names]
    
    return jsonify({"marks": marks})

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
