import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.sign_up import *
from lib.user import *
from lib.listing import *
from lib.listing_repository import *
from lib.request_repository import RequestRepository
from lib.request import Request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# @app.route('/test', methods=['GET'])
# def get_test():
#     return render_template('test.html')

#AMY AND SEAN'S CODE
# This function gathers all of the details for sign up
@app.route('/login', methods=["POST"])
def submit_signup():
    connection = get_flask_database_connection(app)
    userRepo = UserRepository(connection)
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    userRepo.create(name, email, password)
    return render_template('login.html', name=name, email=email, password=password)

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/loggedin', methods=["POST"])
def submit_login():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form['password']
    userRepo = UserRepository(connection)
    checker = userRepo.check_password(email, password)
    if checker:
        id = userRepo.get_userid(email, password)
        name = userRepo.get_username(email, password)
        return render_template('loggedin.html', id=id, name = name, email=email, password=password)
    else:
        message = "Incorrect details" 
        return render_template('login.html', message = message)

@app.route('/adminlogin', methods=['GET'])
def loggedin_page():
    return render_template('loggedin.html')



#----------------------------------------------#
#Bookings
@app.route('/book', methods=['GET'])
def booking_page():
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    #testing authentication
    id = request.args['id']
    listings = repo.get()
    return render_template('booking.html', id=id, listings=listings)

@app.route('/requests', methods=['GET'])
def request_page():
    #testing authentication
    id = request.args['id']
    return render_template('requests.html', id=id)

@app.route('/listing/<int:id>', methods=['POST'])
def submit_request(id):
    connection = get_flask_database_connection(app)
    date_from = request.form['date_from']
    date_to = request.form['date_to']
    user_id = request.args['id']
    listing_id = request.form['listing_id']
    req_repo = RequestRepository(connection)
    list_repo = ListingRepository(connection)
    booking = Request(None, date_from, date_to, user_id, listing_id, confirmed=True)
    listing = list_repo.select(id)
    # Run check to see if date available then run if block
    if req_repo.check_dates(date_from, date_to, listing_id):
        booking = req_repo.create_request(booking)
        return redirect(f'/your_booking/{booking.id}')
    else:
        message = 'Booking failed. Dates not available.'
        return render_template('listing.html', message=message, listing=listing)

@app.route('/your_booking/<int:id>', methods=['GET'])
def your_booking(id):
    connection = get_flask_database_connection(app)
    list_repo = ListingRepository(connection)
    req_repo = RequestRepository(connection)
    booking = req_repo.get_single_requests(id)
    listing = list_repo.select(booking.listing_id)
    # Working out the total price of the booking
    total_days = booking.date_to - booking.date_from
    cost = "{:.2f}".format(total_days.days * listing.price)
    return render_template('booking_success.html', listing=listing, booking=booking, cost=cost)

#ROBERT AND HARRY'S CODE
@app.route('/create', methods=['GET'])
def get_data():
    id = request.args['id']
    return render_template('create.html', id=id)

@app.route('/create', methods=['POST'])
def post_data():
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    title = request.form['title']
    description = request.form['description']
    price = request.form['price']
    user_id = request.args['id']
    listing = Listing(None, title, description, price, user_id)
    listing = repo.insert(listing)
    return redirect(f'/listing/{listing.id}')

@app.route('/listing/<int:id>', methods=['GET'])
def get_listing(id):
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    listing = repo.select(id)
    return render_template('listing.html', listing=listing)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))