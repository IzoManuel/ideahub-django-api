#!/bin/bash
NUM_RECORDS=${1:-10}  # Default to 10 records if no argument is provided
python manage.py populate_db $NUM_RECORDS --settings=settings.local
