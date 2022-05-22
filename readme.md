# Pharmacy management system

## Features
- New Inventory with automatic composition fetch
- Billing with alternative suggestion management
- Bill with dedicated UPI Qr code to pay the bill with Grand total embedded
- Retrival of old bills by bill number
- Admin Dashboard
- Sales Analytics with daily, monthly revenue measures and most demanded medicine with total revenue collected till date
- Admin can view Inventory.
- Can view old inventory
- Option to take database backup for future revert back point
- Pharmacy profile with ability to change and update.

## How to execute
```
git clone 
cd medical
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```