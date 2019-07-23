from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError

def greater_than_zero(field):
    if field.data <=0:
        raise ValidationError('Debe ser un número positivo')


class CompraForm(FlaskForm):
    fecha = DateField('Fecha', validators=[DataRequired('Campo obligatorio')])
    concepto = StringField('Concepto', validators=[DataRequired('Campo obligatorio')])
    cantidadComprada = FloatField('Cantidad Comprada', validators=[DataRequired('Campo obligatorio')])
    monedaComprada = SelectField('Moneda', choices=[('EUR', 'Euros'), ('BTC', 'Bitcoins'), ('LTC', 'Litecoins'), ('ETH', 'Ethereum')])
    cantidadPagada = FloatField('Cantidad Pagada', validators=[DataRequired('Campo obligatorio'), greater_than_zero])
    monedaPagada = SelectField('Moneda', choices=[('EUR', 'Euros'), ('BTC', 'Bitcoins'), ('LTC', 'Litecoins'), ('ETH', 'Ethereum')])
    submit = SubmitField('Comprar')

    def validate_cantidadComprada(self, field):
        if field.data < 0:
            raise ValidationError('Debe ser un número positivo')

class UpdateForm(FlaskForm):
    ix = IntegerField('ix', validators=[DataRequired('Campo obligatorio')])
    fecha = StringField('Fecha', validators=[DataRequired('Campo obligatorio')])
    concepto = StringField('Concepto', validators=[DataRequired('Campo obligatorio')])
    cantidadComprada = FloatField('Cantidad Comprada', validators=[DataRequired('Campo obligatorio'), greater_than_zero])
    monedaComprada = SelectField('Moneda', choices=[('EUR', 'Euros'), ('BTC', 'Bitcoins'), ('LTC', 'Litecoins'), ('ETH', 'Ethereum')])
    cantidadPagada = FloatField('Cantidad Pagada', validators=[DataRequired('Campo obligatorio'), greater_than_zero])
    monedaPagada = SelectField('Moneda', choices=[('EUR', 'Euros'), ('BTC', 'Bitcoins'), ('LTC', 'Litecoins'), ('ETH', 'Ethereum')])
    submit = SubmitField('Modificar')
