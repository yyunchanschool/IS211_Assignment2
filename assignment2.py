import argparse
import urllib.request
import logging
import datetime
import csv

def downloadData(url):
    """Downloads the data"""
    url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    return data

def processData(data):
    csvData = csv.reader(data)
    personData = {}
    next(csvData)

    for row in csvData:
        try:
            row(2) = datetime.strptime(row(2), '%d/%m/%y')
        except ValueError:
            id = int(row(0))
            line = int(row(0))+1
            logger = logging.getLogger('assignment2')
            logger.error('Error processing line #'[line]' for ID #'[id]", format(line, id))
    return personData

def displayPerson(id, personData):
    try reply = 'Person #'[id]' is '[name]' with a birthday of '[date]'
        print(reply)
    except KeyError:
        print('No user found')

def main(url):
    print(f"Running main with URL = {url}...")

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    logging.basicConfig(filename="errors.log", level=logging.ERROR)
