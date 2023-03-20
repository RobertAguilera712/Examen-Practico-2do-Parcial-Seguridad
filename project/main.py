import os
import uuid
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from project.models import Cubos
from werkzeug.utils import secure_filename
from . import db

main = Blueprint('main',__name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/administrador')
@login_required
@roles_required('admin')
def admin():
    cubos= Cubos.query.all()
    return render_template('productos.html',cubos=cubos)


@main.route('/administrador/agregar', methods=['POST', 'GET'])
@login_required
@roles_required('admin')
def agregar():
    if request.method == 'POST':
        cubos= Cubos.query.all()
        nombre = request.form.get('name')
        descripcion = request.form.get('description')
        precio = request.form.get('precio')
        img=str(uuid.uuid4())+'.png'
        imagen=request.files['imagen']
        ruta_imagen = os.path.abspath('project\\static\\img')
        imagen.save(os.path.join(ruta_imagen,img))       
        cubo= Cubos(nombre,descripcion,precio,img)
        db.session.add(cubo)
        db.session.commit()
        flash('Guardado exitoso')
        return redirect(url_for('main.admin'))
    return render_template('agregar.html')


@main.route('/administrador/eliminar/<id>')
@login_required
@roles_required('admin')
def delete(id):
    cubo=Cubos.query.get(id)
    db.session.delete(cubo)
    db.session.commit()
    flash('Se elimino correctamente')
    return redirect(url_for('main.admin'))


@main.route('/administrador/editar/<id>', methods=['POST', 'GET'])
@login_required
@roles_required('admin')
def update(id):
    cubo=Cubos.query.get(id)
    if request.method == 'POST':
        os.remove('project/static/img/{}'.format(str(cubo.img)))
        imagen=request.files['imagen']
        ruta_imagen = os.path.abspath('project\\static\\img')
        imagen.save(os.path.join(ruta_imagen,cubo.img))       
        cubo.name = request.form.get('name')
        cubo.description = request.form.get('description')
        cubo.precio = request.form.get('precio')
        db.session.commit()  
        flash('Modificación exitosa')
        return redirect(url_for('main.admin'))
    return render_template('editar.html',nombre=cubo.name,precio=int(cubo.precio),
                           descripcion=str(cubo.description),
                           imagen=cubo.img, id=cubo.id)
   

@main.route('/galeria')
@login_required
def galeria():
    cubos= Cubos.query.all()
    return render_template('galeria.html',cubos=cubos)