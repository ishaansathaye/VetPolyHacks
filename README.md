
 upcoming_events = [["Meet and Greet", "Meets every 2 weeks.\nCome meet other veterans\nin your area, and connect with industry professionals!\nAttend for as long as you wish.",
                        "5:00PM-7:00PM", "SLO Health Center: 1495 Palm St,San Luis Obispo,\nCA 93401"], ["Sunday Breakfast", "Enjoy a hearty breakfast with other veterans!", "8:30AM-10:30AM", "Veteran's Hall\n801 Grand Ave, San Luis Obispo,\nCA 93401"]]

    # for i in range(2):
    #     c.execute("INSERT INTO events VALUES (?,?,?,?)",
    #               (upcoming_events[i], descs[i], time[i], location[i]))
    # conn.commit()
    # data = []
    # rows = c.execute("SELECT * FROM events")

    # for row in rows:
    #     data.append(row)

    return render_template('groupPage.html', titles=["Event Name", "Description", "Time", "Location", "Register"], info=upcoming_events)
