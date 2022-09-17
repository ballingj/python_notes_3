import json

import helper


def load_nobel_prizes(filename='prize.json'):
    with open(filename, 'r') as infile:
        data = json.load(infile)  # Parse JSON data
        return data


# My first attempt before using the lambda function
# def filter_by_year(year, prizes):
#     f_by_year = []
#     for prize in prizes:
#         if prize['year'] == year:
#             f_by_year.append(prize)
#     return f_by_year

# def filter_by_cat(prizes):
#     f_by_cat = []
#     for prize in prizes:
#         if prize['category'].lower() == category.lower():
#             f_by_cat.append(prize)
#     return f_by_cat


def main(year, category):
    data = load_nobel_prizes()
    # Add more here!
    prizes = data['prizes']
    if year:
        prizes = filter(lambda prize: prize['year'] == year, prizes)

    if category:
       prizes = filter(lambda prize: prize['category'].lower() == category.lower(), prizes)

    for prize in prizes:
        print(prize)

    print('*'*30)
    print(f"{prize['year']} Nobel Prize in {prize['category'].title()}")
    print('*'*30)
    for laureate in prize['laureates']:
        firstname = laureate['firstname']
        surname = laureate.get('surname', '')
        print(f"{firstname} {surname}: {laureate['motivation']}")


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)
