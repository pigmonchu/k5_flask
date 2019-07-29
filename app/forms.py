from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError
import sqlite3

def greater_than_zero(form, field):
    if field.data <=0:
        raise ValidationError('Debe ser un número positivo')

def consultaMonedas():
    conn = sqlite3.connect('data/movimientos.db')
    cursor = conn.cursor()

    query = '''
            SELECT id, name FROM monedas;
            '''

    rows = cursor.execute(query) #Luis se va a la fruteria y deja las patatas en rows

    resp = []
    for row in rows:
        resp.append(row)

    print(resp)
    conn.close()
    return resp

class CompraForm(FlaskForm):
    _monedas = consultaMonedas()
    fecha = DateField('Fecha', validators=[DataRequired('Campo obligatorio')])
    concepto = StringField('Concepto', validators=[DataRequired('Campo obligatorio')])
    cantidadComprada = FloatField('Cantidad Comprada', validators=[DataRequired('Campo obligatorio')])
    monedaComprada = SelectField('Moneda', choices=_monedas)
    cantidadPagada = FloatField('Cantidad Pagada', validators=[DataRequired('Campo obligatorio'), greater_than_zero])
    monedaPagada = SelectField('Moneda', choices=_monedas)
    submit = SubmitField('Comprar')

    def validate_cantidadComprada(self, field):
        if field.data < 0:
            raise ValidationError('Debe ser un número positivo')
    

class UpdateForm(FlaskForm):
    _monedas = consultaMonedas()
    ix = IntegerField('ix', validators=[DataRequired('Campo obligatorio')])
    fecha = StringField('Fecha', validators=[DataRequired('Campo obligatorio')])
    concepto = StringField('Concepto', validators=[DataRequired('Campo obligatorio')])
    cantidadComprada = FloatField('Cantidad Comprada', validators=[DataRequired('Campo obligatorio'), greater_than_zero])
    monedaComprada = SelectField('Moneda', choices=_monedas)
    cantidadPagada = FloatField('Cantidad Pagada', validators=[DataRequired('Campo obligatorio'), greater_than_zero])
    monedaPagada = SelectField('Moneda', choices=_monedas)
    submit = SubmitField('Modificar')
