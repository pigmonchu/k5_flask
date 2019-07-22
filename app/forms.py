from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class CompraForm(FlaskForm):
    fecha = DateField('Fecha', validators=[DataRequired()])
    concepto = StringField('Concepto', validators=[DataRequired()])
    cantidadComprada = FloatField('Cantidad Comprada', validators=[DataRequired()])
    monedaComprada = SelectField('Moneda', choices=[('EUR', 'Euros'), ('BTC', 'Bitcoins'), ('LTC', 'Litecoins'), ('ETH', 'Ethereum')])
    cantidadPagada = FloatField('Cantidad Pagada', validators=[DataRequired()])
    monedaPagada = SelectField('Moneda', choices=[('EUR', 'Euros'), ('BTC', 'Bitcoins'), ('LTC', 'Litecoins'), ('ETH', 'Ethereum')])
    submit = SubmitField('Comprar')

    def validate_cantidadComprada(self, field):
        if field.data < 0:
            raise ValidationError('Debe ser un número positivo')