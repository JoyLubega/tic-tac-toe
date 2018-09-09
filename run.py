from api.views import app


if __name__ == "__main__":
    # app.run(debug=True)
    app.test_client().get('/');