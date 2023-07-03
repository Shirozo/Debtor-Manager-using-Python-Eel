from datetime import datetime
from dateutil.relativedelta import relativedelta

date_after_month = datetime.today()+ relativedelta(months=1)
print('Today: ',datetime.today().strftime('%d/%m/%Y'))
print('After Month:', date_after_month.strftime('%d/%m/%Y'))