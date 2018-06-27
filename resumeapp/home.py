from flask import Blueprint, render_template, send_from_directory

homeapp = Blueprint('homeapp', __name__)

directory = r'/home/phillip/projects/resumeflask/files'

@homeapp.route('/')
def home():
    return render_template('index.html')

@homeapp.route('/resumeData.json')
def data():
    return send_from_directory(directory=directory, filename='resumeData.json')

@homeapp.route('/profilepic/<filename>')
def profile(filename):
    return send_from_directory(directory=directory, filename=filename)


@homeapp.route('/resume')
def resume():
    return send_from_directory(directory=directory, filename='RESUME.pdf')

@homeapp.route('/dashboard/<filename>')
def dashboard(filename):
    return send_from_directory(directory=directory + r'/dashboard', filename=filename)

@homeapp.route('/service-worker.js')
def service_worker():
    return send_from_directory(directory=directory, filename='service-worker.js')

@homeapp.route('/images/loader.gif')
def image_loader():
    return send_from_directory(directory=directory, filename='loader.gif')

@homeapp.route('/static/images/overlay-bg.png')
def overlay_bg():
    return send_from_directory(directory=directory, filename='overlay-bg.png')
