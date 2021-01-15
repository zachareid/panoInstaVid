@app.route('/id/<my_id>')
def id(my_id):
    if not os.path.exists("./videos/" + my_id + ".mp4"):
        return "File doesn't exist or isn't ready. Be patient :^)"
    else:
        return "<html> here's ur file ma'am. <a href='/download/1610568282240902'> Here ya go </a></html>"

@app.route('/download/<id>')
def download(id):
    my_dir = "./videos/"
    return send_from_directory(my_dir, id + ".mp4")


@app.route('/email')
def email():
    msg = Message("Hello",
                  sender="zacreid45@gmail.com",
                  recipients=["zac.reid45@icloud.com"])
    with app.open_resource("./videos/1610569176263521.mp4") as fp:
        msg.attach("vid.mp4","video/mp4", fp.read())
    mail.send(msg)
    return "nice"
