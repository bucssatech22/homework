from flask import Flask, render_template, request, redirect, session, url_for

def input_item():
    if request.method == 'POST':
        item = request.form['item']
        session['items'] = item
        return redirect(url_for('input_item'))
    return render_template("input_item.html")