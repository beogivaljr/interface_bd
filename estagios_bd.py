from firebase import Firebase


if __name__ == '__main__':
    config = {
        "apiKey": "AIzaSyAd5C78W8YcEVhWHHtJPVcKb3QMxLnTU-k",
        "authDomain": "projetobd-b2fd9.firebaseapp.com",
        "databaseURL": "https://projetobd-b2fd9.firebaseio.com",
        "storageBucket": "projetobd-b2fd9.appspot.com"
    }

    firebase = Firebase(config)

    # Get a reference to the auth service
    auth = firebase.auth()

    # Log the user in
    user = auth.sign_in_with_email_and_password('admin.bd@gmail.com', '123456')

    # Get a reference to the database service
    db = firebase.database()

    # data to save
    data = {
        "name": "Joe Boi"
    }

    # Pass the user's idToken to the push method
    # results = db.child("Aluno").push(data, user['idToken'])
    results = db.child('Aluno').child('8041564').set(data)
    print(results)
